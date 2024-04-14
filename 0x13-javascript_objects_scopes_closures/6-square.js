#!/usr/bin/node
// print function with customized chars to print square

const FormerSquare = require('./5-square');

module.exports = class Square extends FormerSquare {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

