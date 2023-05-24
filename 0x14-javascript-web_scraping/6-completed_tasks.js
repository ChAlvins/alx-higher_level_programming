#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let responsedata;
const dict = {};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    responsedata = JSON.parse(body);
    responsedata.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dict)) {
          dict[userid] = 0;
        } else {
          dict[userid] += 1;
        }
      }
    });
    console.log(dict);
  }
});
