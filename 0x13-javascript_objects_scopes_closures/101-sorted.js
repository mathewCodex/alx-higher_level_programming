#!/usr/bin/node

const { dict } = require('./101-data');

const convertedArr = Object.entries(dict);

const newObj = {};

convertedArr.forEach(elem => {
	newObj[elem[1]] ? newObj[elem[1]].push(elem[0]) : newObj[elem[1]] = [elem[0]];
});

console.log(newObj);
