function magicMatrix(arr) {
    let isMagic = true;
    let lastSum = arr[0].reduce((a, v) => a + v);
    for (let r = 0; r < arr.length; r++) {

        let colSum = 0;
        let rowSum = 0;
        for (let c = 0; c < arr.length; c++) {
            colSum += arr[c][r]
            rowSum += arr[r][c]

        }
        if (colSum !== lastSum || rowSum !== lastSum) {
            isMagic = false;
            break;
        }


    }
    console.log(isMagic);
}

magicMatrix(
    [[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
)

magicMatrix(
    [[11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]]
)