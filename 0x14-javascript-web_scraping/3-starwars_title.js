#!/usr/bin/node

const request = require('request');
const args = process.argv;
const fileId = args[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + fileId;

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
