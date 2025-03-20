#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
    }
  });

  console.log(completedTasks);
});
