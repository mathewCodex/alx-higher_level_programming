#!/usr/bin/node
// status code of a request


const req = require('request');
const url = process.argv[2];
req.get(url, function (err, res) {
	if (err) {
		console.log(err);
	} else {
		console.log('code:' + ' ' + res.statusCode);
	}
});
