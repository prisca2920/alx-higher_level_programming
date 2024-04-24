#!/usr/bin/node

const URL = process.argv[2];
const characterId = 18;
const request = require('request');

request(URL, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body).results;
    const characterMovies = data.filter(movie =>
      movie.characters.some(character =>
        character.endsWith(`/${characterId}/`)
      )
    );
    console.log(characterMovies.length);
  }
});
