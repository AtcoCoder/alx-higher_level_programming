#!/usr/bin/node

const request = require('request');
const args = process.argv;
const movieId = args[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const film = JSON.parse(body);

  const characters = film.characters;

  for (const character of characters) {
    request(character, function (err, res, data) {
      if (err) {
        return console.error(err);
      }
      const characterInfo = JSON.parse(data);
      console.log(characterInfo.name);
    });
  }
});
