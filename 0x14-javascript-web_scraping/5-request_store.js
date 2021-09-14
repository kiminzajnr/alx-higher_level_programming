#!/usr/bin/node
/**
  gets the contents of a webpage and stores it in a file
  usage: ./5-request_store.js <URL to request> <path>
  */
const myArgs = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
request(myArgs[0], function (error, response, body) {
  if (!error) {
    fs.writeFile(myArgs[1], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
