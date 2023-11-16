#!/usr/bin/node

const { list } = require('./100-data');

const mappedList = list.map((element, idx) => element * idx);
console.log(list);
console.log(mappedList);

