#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  // Remove duplicates and sort in descending order
  const uniqueSortedArgs = [...new Set(args)].sort((a, b) => b - a);

  // The second element is the second biggest integer
  const secondBiggest = uniqueSortedArgs[1];
  console.log(secondBiggest || 0);
}
