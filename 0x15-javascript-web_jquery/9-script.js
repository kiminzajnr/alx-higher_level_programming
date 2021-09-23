#!/usr/bin/node
/**
  * fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from the fetch in the HTML tag DIV#hello
  * you must use JQuery
  */
const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (data) {
  const hello = data.hello;
  $('DIV#hello').text(hello);
});
