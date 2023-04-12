#!/usr/bin/node
/*
 * a script that computes and prints a factorial
 * first argument is integer (argument can be cast as integer)
 * used for computing the factorial
 * Factorial of NaN is 1
*/
function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (factorial(number - 1) * number);
  }
}
const number = process.argv[2];
if (number) {
  const result = factorial(number);
  console.log(result);
} else {
  console.log(1);
}
