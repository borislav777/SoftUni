function biggestHalf(arr) {
    arr.sort((a,b) =>a - b);
    return arr.slice(arr.length - Math.round(arr.length / 2));
}

console.log(biggestHalf([3, 19, 14, 7, 2, 19, 6]
    ));