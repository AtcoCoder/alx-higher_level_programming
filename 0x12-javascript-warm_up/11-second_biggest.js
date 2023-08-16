#!/usr/bin/node

function secondBiggest (array) {
  const length = array.length;
  if (length <= 1) {
    console.log(0);
    return;
  }
  const newArray = array.map((element) => element);
  newArray.sort(function(a, b){return a-b});
  newArray.reverse();
  console.log(newArray[1]);
}

const args = process.argv;
const length = args.length;
const array = [];
let index;
for (index = 2; index < length; index++) {
  array.push(parseInt(args[index]));
}
secondBiggest(array);
