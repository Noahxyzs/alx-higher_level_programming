#!/usr/bin/node
// count occurences
exports.nbOccurences = function (list, element) {
  return list.filter(x => x === element).length;
};
