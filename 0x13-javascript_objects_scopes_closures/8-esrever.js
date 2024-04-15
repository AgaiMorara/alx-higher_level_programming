#!/usr/bin/node

// Function that reverses a list
exports.esrever = function (list) {
    let index = list.length;
    let new_list = [];

    while (index) {
        new_list.push(list[index - 1]);
        index--;
    }

    return new_list;
};

