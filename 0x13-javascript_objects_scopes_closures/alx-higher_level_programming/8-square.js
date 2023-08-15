#!/usr/bin/node

const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x += 1) {
    console.log('X'.repeat(size));
  }
}
