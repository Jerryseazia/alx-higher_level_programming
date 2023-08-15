#!/usr/bin/node

const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = num; x > 0; x -= 1) {
    console.log('C is fun');
  }
}
