#!/usr/bin/node
// a script that imports an array and computes a new array.

const oldarray = require('./100-data').list;
const newarray = oldarray.map((x, index) => x * index);
console.log(oldarray);
console.log(newarray);
