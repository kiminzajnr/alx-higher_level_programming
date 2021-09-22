#!/usr/bin/node
/**
  * updates text color of the <header> element to red
  * not allowed to use document.querySelector
  * you must use JQuery API
  */
const $ = window.$;
$(document).ready(function () {
  $('header').css('color', 'red');
});
