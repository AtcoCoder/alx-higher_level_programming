#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;
const url = args[2];
const filePath = args[3];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(filePath, body, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
