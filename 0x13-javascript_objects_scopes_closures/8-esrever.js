#!/usr/bin/node

exports.esrever = function (list) {
  let index;
  const reversedList = [];
  for (index = list.length - 1; index >= 0; index--) {
    reversedList.push(list[index]);
  }
  return reversedList;
};
