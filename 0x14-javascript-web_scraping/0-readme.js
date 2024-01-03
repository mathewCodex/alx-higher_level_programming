#!/usr/bin/node
// using filesytem api

const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf-8',
	function (err, data) {
		if (err) {
			console.log(err);
			return;
		}
		console.log(data);
	});
