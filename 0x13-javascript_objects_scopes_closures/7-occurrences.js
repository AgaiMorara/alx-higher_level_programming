#!/usr/bin/node
//function that returns the number of occurences in a list

exports.nbOccurences = function (list, Element) {
    let count = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === Element) {
            count++;
        }
    }
    return count;
};
