'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let n = nums.length;
    if (n === 1) return nums[0];
    var max = 0;
    var sec = 0;

    for (var i = 0; i < n; i++) {
        if (nums[i] > nums[max]) {
            var tmp = max;
            max = i;
            sec = tmp;
        } else if (nums[i] === nums[max]) {
            if (max === sec) {
                max = i;
                sec = i;
            } else {
                max = i;
            }
        } else {
            if (max === sec) {
                sec = i;
            } else if (nums[i] >= nums[sec]) {
                sec = i;
            }
        }
    }

    return nums[sec];
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}

