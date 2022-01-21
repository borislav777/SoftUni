function equalNeighbors(arr) {
    let counter = 0;
    for (let r = 0; r < arr.length; r++) {
        for (let c = 0; c < arr[r].length; c++) {
            if (arr[r][c] == arr[r][c + 1]) {counter++;}
            if (r !== arr.length - 1 && arr[r][c] == arr[r + 1][c]) {counter++;}

        }
    }
    return counter;
}

console.log(equalNeighbors(
    [['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4']]
));

console.log(equalNeighbors(
    [['test', 'yes', 'yo', 'ho'],
 ['well', 'done', 'yo', '6'],
 ['not', 'done', 'yet', '5']]
));