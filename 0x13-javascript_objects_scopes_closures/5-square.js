#!/usr/bin/node
// a class square that inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
