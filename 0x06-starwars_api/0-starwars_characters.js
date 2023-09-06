#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// API request to get Movie ID
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Analyze the response to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Repeat thru the character URLs and fect character ID
  // Make a request to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Analyze the charcter ID and print the character's name...
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
