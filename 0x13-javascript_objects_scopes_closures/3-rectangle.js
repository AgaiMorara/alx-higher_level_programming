#!/usr/bin/node
// adds an instance method print(), that prints the rectangle using X

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;
      for (; j < this.width; ++j) {
        process.stdout.write('X');
      }
      if (j === this.width) {
        console.log('');
      }
    }
  }
};
