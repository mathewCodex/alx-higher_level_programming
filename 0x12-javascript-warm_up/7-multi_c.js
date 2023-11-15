#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);
const printmyC = quantity => {
	for (; quantity > 0; quantity--)
		console.log('C is fun');
};

Number.isInteger(num) ? printmyC(num) : console.log('Missing Number of occurences');
