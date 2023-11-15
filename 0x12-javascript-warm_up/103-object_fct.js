#!/usr/bin/node

const myObj = {
	type: 'Object',
	value: 12
};

console.log(myObj);

myObj.incr = () => myObj.value++;

myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
