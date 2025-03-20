#!/usr/bin/node
// extract a value from json... first fetch the json

const request =  require('request');
const id = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function(error, response, body) {
    if (error){
	console.error(error);
    }
    console.log(JSON.parse(body).title);
});
