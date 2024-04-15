#!/usr/bin/node

// Function that reverses a list
exports.esrever = function (list) {
  let index = list.length;
  const newList = [];

  while (index) {
    newList.push(list[index - 1]);
    index--;
  }

  return newList;
};
