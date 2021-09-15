#!/usr/bin/node
/**
  prints number of movies where the character 'Wedge Antilles' is present.
  usage: ./4-starwars_count.js <API URL>
  */
const myArgs = process.argv.slice(2);
const request = require('request');
const characters_ = [];
request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (!error) {
    let i = 0;
    const json_ = JSON.parse(body);

    for (i = 0; i < 7; i++) {
      characters_.push(json_.results[i].characters);
    }
  }
  let counter = 0;
  characters_.forEach(function each (item) {
    if (Array.isArray(item)) {
      item.forEach(each);
    } else {
      if (item === 'https://swapi-api.hbtn.io/api/people/18/') {
        counter++;
      }
    }
  });
  console.log(counter);
});
