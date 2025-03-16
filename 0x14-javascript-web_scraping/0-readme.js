#!/usr/bin/node

// script that reads and prints the content of a file

let  fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
   console.error("Usage: ./0-readme.js <file-path>");
   process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
   if (err) {
	console.error(err);
	return;
   }
   console.log(data);
});
