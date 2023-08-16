#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stepUp = 0;
    while (stepUp < this.height) {
      let stepRight = 0;
      let step = '';
      for (stepRight = 0; stepRight < this.width; stepRight++) {
        step += 'X';
      }
      console.log(step);
      stepUp++;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
