require('dotenv').config();
const { put, list, del } = require('@vercel/blob');
const fs = require('fs');
const path = require('path');

const EXCLUDED = ['node_modules', 'package.json', 'package-lock.json', 'build.py', '.env', '.gitignore', 'upload-to-vercel.js', 'timestamp.txt'];
const EXCLUDED_DIRS = ['.obsidian', '.git', '.github'];

async function uploadFolder(localPath, remotePrefix = '', timestamp) {
  const entries = fs.readdirSync(localPath, { withFileTypes: true });

  for (const entry of entries) {
    const entryPath = path.join(localPath, entry.name);

    // skip excluded stuff
    if (EXCLUDED.includes(entry.name)) continue;

    if (entry.isDirectory()) {
      if (EXCLUDED_DIRS.includes(entry.name)) continue;
      const remotePath = path.posix.join(remotePrefix, entry.name);
      await uploadFolder(entryPath, remotePath, timestamp);
    } else {
      // modify filename to include timestamp before extension
      const ext = path.extname(entry.name);          // '.md' or '.json'
      const baseName = path.basename(entry.name, ext); // 'filename'
      const timestampedName = `${baseName}.${timestamp}${ext}`; // 'filename.20240624T1530.md'
      const remotePath = path.posix.join(remotePrefix, timestampedName);

      const buffer = fs.readFileSync(entryPath);
      await put(remotePath, buffer, {
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
  for (const blob of blobs) {
    await del(blob.url);
  }
}

async function main() {
  // generate timestamp once
  const timestamp = new Date().toISOString().replace(/[-:]/g, '').slice(0, 15); // e.g. 20240624T1530

  // write timestamp.txt locally
  console.log("timestamp", timestamp)
  fs.writeFileSync('timestamp.txt', timestamp);

  // clear old blobs
  console.log("clearing all");
  await clearAll();

  // upload timestamp.txt (without timestamp in filename)
  const timestampBuffer = Buffer.from(timestamp);
  await put('timestamp.txt', timestampBuffer, {
    access: 'public',
    allowOverwrite: true,
    multipart: true
  });
  console.log(`uploaded: timestamp.txt`);

  // upload rest of files with timestamp suffix
  console.log("uploading all files");
  await uploadFolder('.', '', timestamp);
}

main();
