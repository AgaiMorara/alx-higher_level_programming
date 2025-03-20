#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('usage: ./101-starwars_character.js movieId');
}

request(url, { json: true }, (error, response, body) => {
  if (error) {
    return console.error(error);
  }

  const characters = body.characters;

  let promiseChain = Promise.resolve();

  characters.forEach(characterUrl => {
    promiseChain = promiseChain.then(() =>
      new Promise((resolve) => {
        request(characterUrl, { json: true }, (error, response, body) => {
          if (!error) {
            console.log(body.name);
          }
          resolve();
        });
      })
    );
  });
});
