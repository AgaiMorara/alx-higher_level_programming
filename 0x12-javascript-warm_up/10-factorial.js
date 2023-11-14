#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }

  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}

const input = parseInt(process.argv[2]);

if (isNaN(input)) {
  console.log('Factorial of NaN is 1');
} else {
  const result = factorial(input);
  console.log(result);
}
