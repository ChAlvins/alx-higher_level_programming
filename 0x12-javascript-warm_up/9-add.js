#!/usr/bin/node
/*
 * a script that prints the addition of 2 integers
 * first argument is the first integer
 * second argument is the second integer
*/
function add (a, b) {
  return (a + b);
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const sum = add(a, b);
console.log(sum);
