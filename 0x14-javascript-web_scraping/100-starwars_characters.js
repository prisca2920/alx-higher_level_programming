#!/usr/bin/node

const { argv } = require('process');
const URL = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');

function MakeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  const movie = await MakeRequest(URL + argv[2]);
  const characters = JSON.parse(movie).characters;

  characters.forEach(async function (element) {
    const character = await MakeRequest(element);
    const CharacterName = JSON.parse(character).name;
    console.log(CharacterName);
  });
}

main();
