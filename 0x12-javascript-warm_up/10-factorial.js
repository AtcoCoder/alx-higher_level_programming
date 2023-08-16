#!/usr/bin/node
const number = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return num * factorial(num - 1);
}

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
