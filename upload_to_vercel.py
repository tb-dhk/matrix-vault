import os
import subprocess
import json
from datetime import datetime
from dotenv import load_dotenv
import vercel_blob

load_dotenv()

EXCLUDED = ['node_modules', 'package.json', 'package-lock.json', 'build.py', '.env', '.gitignore', 'upload_to_vercel.py', 'manifest.json']
EXCLUDED_DIRS = ['.obsidian', '.git', '.github', ".trash"]

def get_commit_hash():
    if not os.path.exists('manifest.json'):
        return None
    try:
        with open('manifest.json', 'r') as f:
            data = json.load(f)
        # Look for the canonical manifest entry
        manifest_entry = data.get('manifest.json')
        if manifest_entry and manifest_entry.endswith('.json') and manifest_entry.startswith('manifest.'):
            # Extract the hash from "manifest.<hash>.json"
            hash_part = manifest_entry[len('manifest.'):-len('.json')]
            if hash_part:
                print(f"Found last successful commit in manifest: {hash_part}")
                return hash_part
    except Exception as e:
        print(f"Could not read manifest: {e}")
    return None

def get_changed_files():
    """Get list of files changed since the last push (against upstream branch)"""
    try:
        # Diff between upstream and current HEAD
        output = subprocess.check_output(
            ['git', 'diff', '--name-only', get_commit_hash(), 'HEAD'],
            text=True
        )
        return [f for f in output.splitlines() if f]
    except subprocess.CalledProcessError:
        # No upstream (e.g., first push), fallback to full upload
        print("No upstream branch found. Falling back to uploading everything.")
        return None

def refresh_file(manifest, local_path, remote_path):
    old_path = manifest.get(local_path)
    if old_path and old_path != remote_path:
        try:
            vercel_blob.delete(old_path)
            print(f"deleted old version: {old_path}")
        except Exception as e:
            print(f"Could not delete {old_path}: {e}")
    with open(local_path, 'rb') as f:
        vercel_blob.put(remote_path, f.read())
    print(f"uploaded: {remote_path}")


def main(full=False):
    changed_files = get_changed_files()
    is_full_upload = (changed_files is None) or full

    manifest = {}
    if os.path.exists('manifest.json'):
        with open('manifest.json', 'r') as f:
            manifest = json.load(f)

    files_to_upload = []
    if is_full_upload:
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            for file in files:
                if file in EXCLUDED:
                    continue
                local_path = os.path.join(root, file)
                remote_prefix = os.path.dirname(local_path)
                files_to_upload.append((local_path, remote_prefix))
    else:
        for file in changed_files:
            if file in EXCLUDED or not os.path.exists(file):
                continue
            remote_prefix = os.path.dirname(file)
            files_to_upload.append((file, remote_prefix))

    for local_path, remote_prefix in files_to_upload:
        ext = os.path.splitext(local_path)[1]
        base_name = os.path.basename(local_path)
        should_stamp = ext in ['.md', '.json']

        if should_stamp:
            name_without_ext = os.path.splitext(base_name)[0]
            final_name = f"{name_without_ext}.{get_commit_hash()}{ext}"
        else:
            final_name = base_name

        local_path = local_path.lstrip("./")

        remote_path = os.path.join(remote_prefix, final_name).replace('\\', '/')
        remote_path = remote_path.lstrip('./')

        refresh_file(manifest, local_path, remote_path)
        manifest[local_path] = remote_path

    manifest["manifest.json"] = f"manifest.{get_commit_hash()}.json"

    json.dump(manifest, open("manifest.json", "w"), indent=2)
    vercel_blob.delete("manifest.json")
    with open("manifest.json", 'rb') as f:
        vercel_blob.put(f"manifest.{get_commit_hash()}.json", f.read())
    print(f"uploaded: manifest.{get_commit_hash()}.json")

if __name__ == "__main__":
    main()
