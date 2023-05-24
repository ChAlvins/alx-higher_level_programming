#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let responsejson;
let movieid = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    responsejson = JSON.parse(body);
    responsejson.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const split = character.split('/');
        if (split[split.length - 2] === '18') {
          movieid++;
        }
      });
    });
    console.log(movieid);
  }
});
