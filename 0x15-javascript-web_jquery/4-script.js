#!/usr/bin/node
/**
  * toggles the class of the <header>element when the user clicks on tag DIV#toggle_header
  * use JQUERY
  */
const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
