#!/usr/bin/node
// A function that increments and calls another function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
