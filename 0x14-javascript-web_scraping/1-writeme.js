#!/usr/bin/node
// script that writes a string to a file

let fs = requie('fs')'
let filePath = process.argv[2];
let content = process.argv[3];

fs.writeFile(filePath, content , 'utf-8', (error) => {
	if (error) {
	console.log(error);
	return;
	}
});
