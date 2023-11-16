#!/usr/bin/node

class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.height = h;
			this.width = w;
		}
}

print () {
	for (let i = 0; i < this.height; i++)
	{
		console.log('X'.repeat(this.width));
	}
}

rotate () {
	const temp = this.height;
	this.height = this.width;
	this.width = temp;
}

double () {
	this.height = this.height * 2;
	this.width = this.width * 2;
}
}

module.exports = Rectangle;
