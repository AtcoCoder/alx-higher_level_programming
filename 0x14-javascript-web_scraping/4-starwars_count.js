#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  let count = 0;
  if (error) {
    return console.error(error);
  }
  const data = JSON.parse(body);
  const films = data.results;

  for (const film of films) {
    const characters = film.characters;
    if (characters.includes(wedgeAntilles)) {
      count += 1;
    }
  }
  console.log(count);
});
