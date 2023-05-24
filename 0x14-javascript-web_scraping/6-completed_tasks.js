#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    const completedTasks = {};
    const todos = JSON.parse(body);
    for (const i in todos) {
      const todo = todos[i];
      if (todo.completed === true) {
        if (completedTasks[todo.userId] === undefined) {
          completedTasks[todo.userId] = 1;
        } else {
          completedTasks[todo.userId]++;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.error(error);
  }
});
