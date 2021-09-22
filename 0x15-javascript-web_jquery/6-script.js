#!/usr/bin/node
/**
  * updates the text of the <header> element to New Heade!!! when the user clicks on DIV#update_header
  * you must use JQuery API
  */
const $ = window.$;
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
