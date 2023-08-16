#!/usr/bin/node

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fs = require('fs');
let fromA = '';
let fromB = '';
let toC = '';

fs.readFile(fileA, (err, inputA) => {
  if (err) {
    throw err;
  }
  fromA = inputA.toString();

  fs.readFile(fileB, (err, inputB) => {
    if (err) {
      throw err;
    }
    fromB = inputB.toString();
    toC = fromA + fromB;
    fs.writeFile(fileC, toC, (err) => {
      if (err) throw err;
      fromB = inputB.toString();
    });
  });
});
