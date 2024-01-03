#!/usr/bin/node
//scrapper webber

const req = require('request');

req.get(process.argv[2], { json: true }, (error, response, body) => {
	if (error) {
		console.log(error);
		return;
	}

	const taskCompleted = {};
	body.forEach((todo) => {
		if (todo.completed) {
			if (!taskCompleted[todo.useId]) {
				taskCompleted[todo.userId] = 1;
			} else {
				taskCompleted[todo.userId] += 1;
			}
		}
	});
	console.log(taskCompleted);
});
