#!/usr/bin/node
// extract a value from json... first fetch the json... and do its count

const request = require('request');
const url = process.argv[2];

const countWedgeMovies = () => {
  request(url, { json: true }, (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }

    const count = body.results.filter(movie =>
      movie.characters.some(url => url.endsWith('/18/'))
    ).length;

    console.log(count);
  });
};

countWedgeMovies();
