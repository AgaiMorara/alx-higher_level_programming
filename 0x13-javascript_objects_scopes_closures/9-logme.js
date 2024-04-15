#!/usr/bin/node
// function that printes the number of argguments already printed and the new argument value

let count = 0;

exports.logMe = function (item) {
    console.log(`${count++}: ${item}`);
};
