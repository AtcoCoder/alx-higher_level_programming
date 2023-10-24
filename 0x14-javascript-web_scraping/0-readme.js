#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const filePath = args[2];
fs.readFile(filePath, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
