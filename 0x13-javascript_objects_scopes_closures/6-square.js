#!/usr/bin/node
// a class Square that defines a square and inherits from Square of 5-square.js

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (!c) {
      c = 'X';
    } else {
      this.print(c);
    }
  }
};
