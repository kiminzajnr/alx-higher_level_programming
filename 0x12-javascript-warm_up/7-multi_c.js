#!/usr/bin/node
const myArgs = process.argv.slice(2);
let i = 0;
if (isNaN(myArgs[0])) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(myArgs[0])) {
    console.log('C is fun');
    i++;
  }
}
