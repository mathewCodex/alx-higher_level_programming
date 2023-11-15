#!/usr/bin/node

const { argv } = require('process');
const size = parseInt(argv[2]);

const printSqr = (size) => {
	const row = 'X'.repeat(size);
	for (let i = 0; i < size; i++)
		console.log(row);
};
Number.isInteger(size) ? printSqr(size) : console.log('Missing size');
