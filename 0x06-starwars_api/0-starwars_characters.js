#!/usr/bin/node
//  a script that prints all characters of a Star Wars movie

const util = require('util');
const request = util.promisify(require('request'));
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

async function getCharacterName (characterUrl) {
  const response = await request(characterUrl);
  const name = JSON.parse(response.body).name;
  return name;
}

async function fetchAndPrintCharacters () {
  const response = await request(url);
  const charactersUrl = JSON.parse(response.body).characters;
  const characterNames = await Promise.all(charactersUrl.map(getCharacterName));
  characterNames.forEach(name => console.log(name));
}

fetchAndPrintCharacters();
