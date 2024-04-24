#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const complete = {};
    data.forEach(task => {
      if (task.completed) {
        if (complete[task.userId]) {
          complete[task.userId]++;
        } else {
          complete[task.userId] = 1;
        }
      }
    });
    console.log(complete);
  }
});
