#!/usr/bin/node
const request = require('request');
const movieid = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieid;
let data;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
