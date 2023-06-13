#!/usr/bin/node
// converter
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
