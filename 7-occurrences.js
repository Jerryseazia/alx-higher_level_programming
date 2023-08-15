#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numb = 0;
  for (let t in list) {
    if (list[t] === searchElement) {
      numb++;
    }
  }
  return numb;
};
