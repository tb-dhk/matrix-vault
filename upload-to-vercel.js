import 'dotenv/config';
import { put } from '@vercel/blob';
import fs from 'fs';
import path from 'path';

const EXCLUDED = ['node_modules', 'package.json', 'package-lock.json', 'build.py', '.env', '.gitignore', 'upload-to-vercel.js'];
const EXCLUDED_DIRS = ['.obsidian', '.git', '.github'];

async function uploadFolder(localPath, remotePrefix = '') {
  const entries = fs.readdirSync(localPath, { withFileTypes: true });

  for (const entry of entries) {
    const entryPath = path.join(localPath, entry.name);
    const remotePath = path.posix.join(remotePrefix, entry.name);

    if (EXCLUDED.includes(entry.name)) continue;

    if (entry.isDirectory()) {
      if (EXCLUDED_DIRS.includes(entry.name)) continue; 
      await uploadFolder(entryPath, remotePath);
    } else {
      const buffer = fs.readFileSync(entryPath);
      const result = await put(remotePath, buffer, {
        access: 'public',
        allowOverwrite: true,
        multipart: true
      });
      console.log(`✅ Uploaded: ${remotePath} → ${result.url}`);
    }
  }
}

async function main() {
  await uploadFolder('.', '');                   
}

main();
