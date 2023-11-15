#!/usr/bin/node

const myObject = {
	type: 'Object',
	value: 12
};

console.log(myObject);

myObject.incr = () => myObject.value++;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
