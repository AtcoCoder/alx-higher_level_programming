#!/usr/bin/node

module.exports = class Rectangle {

	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;

		}
	}

	print() {
		let step_h = 0;
		while (step_h < this.height) {
			let step_w = 0;
			let step = '';
			for (step_w = 0; step_w < this.width; step_w++) {
				step += 'X';
			}
			console.log(step);
			step_h++;
		}
	}
}
