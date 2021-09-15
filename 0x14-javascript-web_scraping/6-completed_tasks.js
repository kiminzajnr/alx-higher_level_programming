#!/usr/bin/node
/**
  compute number of tasks completed by user id
  usage: /6-completed_tasks.js <API URL>
  */
const myArgs = process.argv.slice(2);
const request = require('request');
const id_ = [];
const result = {};
request(myArgs[0], function (error, response, body) {
  let i;
  if (!error) {
    const json_ = JSON.parse(body);
    const len = json_.length;
    for (i = 0; i < len; i++) {
      if (json_[i].completed) {
        id_.push(json_[i].userId);
      }
    }
    for (let j = 0; j < id_.length; ++j) {
      if (!result[id_[j]]) { result[id_[j]] = 0; }
      ++result[id_[j]];
    }
  }
  console.log(result);
});
