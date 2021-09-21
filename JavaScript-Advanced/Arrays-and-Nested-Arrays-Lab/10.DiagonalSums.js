function diagonalSum(arr) {
    let firstDiagonal = 0;
    let secondDiagonal = 0;
    const size = arr.length - 1;
    for (let i = 0; i < arr.length; i++) {
        firstDiagonal += arr[i][i];
        secondDiagonal += arr[i][size - i];

    }
    console.log(firstDiagonal,secondDiagonal);
}

diagonalSum(
    [[20, 40],
    [10, 60]]

)

diagonalSum(
    [[3, 5, 17],
 [-1, 7, 14],
 [1, -8, 89]]
)