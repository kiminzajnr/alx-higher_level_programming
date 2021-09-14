#!/usr/bin/node
/**
  display the status code of a GET request
  usage: ./2-statuscode.js <URL to request>
  first arguments is the URL to request
  */
const myArgs = process.argv.slice(2);
const request = require('request');
request(myArgs[0], function (error, response, body) {
  if (!error && response) {
    console.log('code:', response.statusCode);
  }
});
