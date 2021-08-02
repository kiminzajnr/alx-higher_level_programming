#!/usr/bin/node
const myArgs = process.argv.slice(2);
let result = 0;
function add (a, b) {
  result = a + b;
  return result;
}
add(parseInt(myArgs[0]), parseInt(myArgs[1]));
console.log(result);
