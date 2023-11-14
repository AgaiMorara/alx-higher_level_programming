#!/usr/bin/node
let x = process.argv[2];
if (isNaN(parseInt(x))) { console.log('Missing number of occurrences'); }

while (x--) { console.log('C is fun'); }
