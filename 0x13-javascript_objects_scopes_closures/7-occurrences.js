#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let elementCount = 0;
  let index;
  for (index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      elementCount++;
    }
  }
  return elementCount;
};
