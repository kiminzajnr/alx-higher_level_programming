#!/usr/bin/node
/**
  reads and prints the content of a file
  first argument is the file path
 */
const myArgs = process.argv.slice(2);
const fs = require('fs');
fs.readFile(myArgs[0], 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
