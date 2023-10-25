#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const wedgeAntilles = '18';

request(url, function (error, response, body) {
  let count = 0;
  if (error) {
    return console.error(error);
  }
  const data = JSON.parse(body);
  const films = data.results;

  for (const film of films) {
    const characters = film.characters;
    for (const character of characters) {
      if (character.includes(wedgeAntilles)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
