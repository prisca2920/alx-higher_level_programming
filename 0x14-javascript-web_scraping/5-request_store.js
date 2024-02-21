#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request.get(URL, (error, reponse, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', error => {
      if (error) {
        console.log(error);
      }
    });
  }
});
