#!/usr/bin/node

exports.add = function (number, theFunction) {
  theFunction(++number);
};
