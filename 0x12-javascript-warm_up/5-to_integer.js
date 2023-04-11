#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
*/
const int = parseInt(process.argv[2]);
if (int) {
  console.log('My number: ' + int);
} else {
  console.log('Not a number');
}
