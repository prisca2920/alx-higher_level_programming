#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial (a) {
  if (!a) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

console.log(factorial(arg));
