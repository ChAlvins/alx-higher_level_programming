#!/usr/bin/node
/*
 * a script that searches the second biggest integer in the list of arguments
 * If no argument passed, print 0
 * If no argument passed, print 0
*/
const argv = process.argv;
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const array = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
