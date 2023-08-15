#!/usr/bin/node

let firstArgument = parseInt(process.argv[2]);

if (isNaN(firstArgument)) {
	console.log('Missing size');
} else if (firstArgument > 0) {
	let count = 0;
	while (count < firstArgument) {
		let secondCount = 0;
		let pixels = '';
		while (secondCount < firstArgument) {
			pixels += 'X';
			secondCount++;
		}
		console.log(pixels);
		count++;
	}
}
