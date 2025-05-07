#!/usr/bin/node
// a script that writes to a file
const fs = require('fs');
const filePath = process.argv[2];
let content = process.argv[3];

if (!filePath) {
  console.log('Usage:' + '<./1-writeme.js> <content>');
}

if (!content) {
  content = '';
}

fs.writeFile(filePath,content ,'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
