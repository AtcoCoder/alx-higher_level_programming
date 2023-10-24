#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
