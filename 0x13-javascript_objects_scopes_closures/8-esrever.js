#!/usr/bin/node

exports.esrever = function (list) {
  let begin = 0;
  let end = list.length - 1;
  while (begin < end) {
    let temp = list[begin];
    list[begin] = list[end];
    list[end] = temp;
    begin++;
    end--;
  }
  return list;
};
