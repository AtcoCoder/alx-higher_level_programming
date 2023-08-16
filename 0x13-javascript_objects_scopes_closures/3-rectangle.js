#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shepUp = 0;
    while (shepUp < this.height) {
      let stepRight = 0;
      let step = '';
      for (stepRight = 0; stepRight < this.width; stepRight++) {
        step += 'X';
      }
      console.log(step);
      shepUp++;
    }
  }
};
