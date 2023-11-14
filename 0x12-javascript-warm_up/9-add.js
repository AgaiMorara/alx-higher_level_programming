#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstarg = parseInt(process.argv[2]);
const secondarg = parseInt(process.argv[3]);

if (isNaN(firstarg) || isNaN(secondarg)) {
  console.log('Missing or invalid input. Please provide two integers.');
} else {
  const result = add(firstarg, secondarg);
  console.log(firstarg + ' + ' + secondarg + ' = ' + result);
}
