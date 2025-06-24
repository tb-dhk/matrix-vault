require('dotenv').config();
const { put } = require('@vercel/blob');
const fs = require('fs');
const path = require('path');

const EXCLUDED = ['node_modules', 'package.json', 'package-lock.json', 'build.py', '.env', '.gitignore', 'upload-to-vercel.js'];
const EXCLUDED_DIRS = ['.obsidian', '.git', '.github'];

async function uploadFolder(localPath, remotePrefix = '') {
  const entries = fs.readdirSync(localPath, { withFileTypes: true });

  const timestamp = new Date().toISOString().replace(/[-:]/g, '').slice(0,15); // e.g. 20240624T1530

  for (const entry of entries) {
    const entryPath = path.join(localPath, entry.name);

    // skip excluded stuff
    if (EXCLUDED.includes(entry.name)) continue;

    if (entry.isDirectory()) {
      if (EXCLUDED_DIRS.includes(entry.name)) continue;
      const remotePath = path.posix.join(remotePrefix, entry.name);
      await uploadFolder(entryPath, remotePath);
    } else {
      // modify filename to include timestamp before extension
      const ext = path.extname(entry.name);          // '.md' or '.json'
      const baseName = path.basename(entry.name, ext); // 'filename'
      const timestampedName = `${baseName}.${timestamp}${ext}`; // 'filename.20240624T1530.md'
      const remotePath = path.posix.join(remotePrefix, timestampedName);

      const buffer = fs.readFileSync(entryPath);
      const result = await put(remotePath, buffer, {
        access: 'public',
        allowOverwrite: true,
        multipart: true
      });
      console.log(`uploaded: ${remotePath}`);
    }
  }
}

async function clearAll() {
  const { blobs } = await list();
  for (const blobPath of blobs) {
    await del(blobPath);
  }
}

async function main() {
  console.log("clearing all")
  await clearAll();

  console.log("uploading all")
  await uploadFolder('.', '');
}

main().catch(console.error);
