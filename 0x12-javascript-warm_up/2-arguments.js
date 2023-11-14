#!/usr/bin/node
const totalags = process.argv.length - 2;

if (totalags === 0) {
  console.log('No argument');
} else if (totalags === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
