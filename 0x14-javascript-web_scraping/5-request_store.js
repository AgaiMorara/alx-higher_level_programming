#!/usr/bin/node
const request = require('request');
const { createWriteStream } = require('fs');

const url = process.argv[2];
const outputFile = process.argv[3];

request(url).pipe(createWriteStream(outputFile));
