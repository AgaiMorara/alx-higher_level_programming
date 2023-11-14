#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstarg = parseInt(process.argv[2]);
const secondarg = parseInt(process.argv[3]);
const result = add(firstarg, secondarg);

if (process.argv.length < 4) { console.log(result); } else { console.log(firstarg + ' + ' + secondarg + ' = ' + result); }
