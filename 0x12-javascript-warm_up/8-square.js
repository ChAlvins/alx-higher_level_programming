#!/usr/bin/node
/*
 * a script that prints a square
 * the first argument is the size of the square
*/
const size = process.argv[2];
if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
