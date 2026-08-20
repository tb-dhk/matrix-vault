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
    try:
        cmd = ['git', 'rev-parse', 'HEAD']
        return subprocess.check_output(cmd, text=True).strip()
    except subprocess.CalledProcessError:
        return None

def upstream():
    if not os.path.exists('manifest.json'):
        return None
    with open('manifest.json', 'r') as f:
        data = json.load(f)
    return data["manifest.json"].split(".")[1]

def get_changed_files():
    """Get list of files changed since the last push (against upstream branch)"""
    try:
        # Diff between upstream and current HEAD
        output = subprocess.check_output(
            ['git', 'diff', '--name-only', upstream(), 'HEAD'],
            text=True
        )
        return [f for f in output.splitlines() if f]
    except subprocess.CalledProcessError:
        # No upstream (e.g., first push), fallback to full upload
        print("No upstream branch found. Falling back to uploading everything.")
        return None

def refresh_file(manifest, local_path, remote_path):
    print("now uploading", remote_path)
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
    if not is_full_upload:
        print("changed files: ", changed_files)

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
            if file in EXCLUDED or any(file.startswith(i) for i in EXCLUDED_DIRS) or not os.path.exists(file):
                continue
            remote_prefix = os.path.dirname(file)
            files_to_upload.append((file, remote_prefix))

    for local_path, remote_prefix in files_to_upload:
        ext = os.path.splitext(local_path)[1]
        base_name = os.path.basename(local_path)

        name_without_ext = os.path.splitext(base_name)[0]
        final_name = f"{name_without_ext}.{get_commit_hash()}{ext}"

        if local_path.startswith("./"):
            local_path = local_path[2:]

        remote_path = os.path.join(remote_prefix, final_name).replace('\\', '/')
        if remote_path.startswith("./"):
            remote_path = remote_path[2:]

        refresh_file(manifest, local_path, remote_path)
        manifest[local_path] = remote_path

    local_manifest = "manifest.json"
    remote_manifest = f"manifest.{get_commit_hash()}.json"

    print("now uploading", remote_manifest)
    old_manifest = manifest.get("manifest.json") # get old_manifest before reassigning
    manifest[local_manifest] = remote_manifest

    if old_manifest and old_manifest != remote_manifest:
        try:
            vercel_blob.delete(old_manifest)
            print(f"deleted old version: {old_manifest}")
        except Exception as e:
            print(f"Could not delete {old_manifest}: {e}")
    with open(local_manifest, 'rb') as f:
        vercel_blob.put(remote_manifest, f.read())
    print(f"uploaded: {remote_manifest}")

    json.dump(manifest, open("manifest.json", "w"), indent=2)

if __name__ == "__main__":
    main()
