#!/usr/bin/node

const superSquare = require('./5-square');

module.exports = class Square extends superSquare {
  charPrint (c) {
    let stepUp = 0;
    while (stepUp < this.width) {
      let stepRight;
      let step = '';
      let charSymbol = 'X';
      if (c) {
        charSymbol = c;
      }
      for (stepRight = 0; stepRight < this.width; stepRight++) {
        step += charSymbol;
      }
      console.log(step);
      stepUp++;
    }
  }
};
