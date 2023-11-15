#!/usr/bin/node

const { argv } require('process');
const args = argv.slice(2);
let result = 0;
let finalArr = [];

if (args.length > 1)
{
	finalArr = [...new Set(args.map((e) => parseInt(e)).sort((a, b) => b - a))];
	result = finalArr.length > 1 ? finalArr[1] : finalArr[0];
}

console.log(result);
