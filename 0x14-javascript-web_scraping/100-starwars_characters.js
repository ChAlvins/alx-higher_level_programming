#!/usr/bin/node
const request = require('request');
const movieid = parseInt(process.argv[2]);
const url = 'https://https://swapi-api.alx-tools.com/api/films/' + movieid;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  const result = movie.characters;
  for (const i of result) {
    request.get(i, function (error, resp, bod) {
      if (error) {
        console.log(error);
      }
      const content = JSON.parse(bod);
      console.log(content.name);
    });
  }
});
