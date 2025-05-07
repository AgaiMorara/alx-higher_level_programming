#!/usr/bin/node
// script that reads and prints the content of a file - the first argument is the file path

const filePath = process.argv[2];

const fs = require('fs');

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
