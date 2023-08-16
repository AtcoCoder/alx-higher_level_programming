#!/usr/bin/node

const firstArgument = parseInt(process.argv[2]);

if (isNaN(firstArgument)) {
  console.log('Missing number of occurrences');
} else if (firstArgument > 0) {
  let count = 0;
  while (count < firstArgument) {
    console.log('C is fun');
    count++;
  }
}
