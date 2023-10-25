#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const tasks = JSON.parse(body);

  const completedTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId] += 1;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
