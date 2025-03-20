#!/usr/bin/node
// Prints all characters of a star wars movie...

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + id, { json: true }, (error, result, body) => {
  if (error) {
    console.error(error);
  }
  const data = body.characters;

  for (const i of data) {
      request(i, { json: true }, (error, result, body) => {
	  if (error) {
        console.error(error);
	    }
	    console.log(body.name);
    });
  }
});
