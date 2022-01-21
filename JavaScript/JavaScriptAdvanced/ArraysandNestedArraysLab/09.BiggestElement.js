function biggestElement(arr) {
    let biggestNumber = Number.MIN_SAFE_INTEGER;
    for (let r = 0; r < arr.length; r++) {
        for (let c = 0; c < arr[r].length; c++) {
            if (arr[r][c] > biggestNumber) {
                biggestNumber = arr[r][c];
            }

        }


    }
    return biggestNumber;
}

console.log(biggestElement(
    [[20, 50, 10],
    [8, 33, 145]]

));

console.log(biggestElement(
    [[3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4]]


));