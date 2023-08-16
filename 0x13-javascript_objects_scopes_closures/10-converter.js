#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (number) {
    if (!isNaN(parseInt(number))) {
      return number.toString(base);
    } else {
      return parseInt(number, base);
    }
  };
};
