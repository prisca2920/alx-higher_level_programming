#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const URL = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
