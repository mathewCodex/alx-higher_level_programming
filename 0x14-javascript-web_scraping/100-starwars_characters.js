#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url, (error, response, body) => {
	if (error) {
		console.log(error);
	} else {
		const content = JSON.parse(body);
		const characters = content.characters;
		for (const xtics of characters) {
			req.get(xtics, (error, response, body) => {
				if (error) {
					console.log(error);
				} else {
					const names = JSON.parse(body);
					console.log(names.name);
				}
			});
		}
	}
});
