#!/usr/bin/node
// script that concats 2 files. The first argument is the file path to the sourcefile

const fs = requier('fs');

const [,, fileA, fileB, fileC] = process.argv;

   if (!fileA || !fileB || !fileC){
      console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
      process.exit(1);
   }

try{
   const contentA = fs.readFileSync(fileA, 'utf8');
   const contentB = fs.readFileSync(fileB, 'utf8');
   fs.writeFileSync = fs.writeFileSync(fileC, contentA + contentB, 'utf8');
} catch(error){
	console.error('Error:', error.message);
	process.exit(1);
}
