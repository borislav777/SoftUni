function diagonalAttack(arr) {
    matrix = arr.reduce((acc, v) => {
        let result = v.split(' ').map((x) => Number(x))
        acc.push(result)
        return acc;
    }, [])
    let firstDiagonal = 0;
    let secondDiagonal = 0;
    let firstDiagonalIndexes = [];
    let secondDiagonalIndexes = [];


    const size = matrix.length - 1;
    for (let i = 0; i < matrix.length; i++) {
        firstDiagonal += Number(matrix[i][i]);
        secondDiagonal += Number(matrix[i][size - i])
        
    }
    if (firstDiagonal === secondDiagonal) {
        for (let r = 0; r < matrix.length; r++) {
            for (let c = 0; c < matrix.length; c++) {
                if (r != c && r != size - c) {
                    matrix[r][c] = firstDiagonal;
                }
            }
        }
    }
    printMatrix(matrix);
    
    function printMatrix(m) {
        for (const el of m) {
            console.log(el.join(' '));
        }
    }
}

diagonalAttack(
    ['5 3 12 3 1',
        '11 4 23 2 5',
        '101 12 3 21 10',
        '1 4 5 2 2',
        '5 22 33 11 1']
)

diagonalAttack(
    ['1 1 1',
'1 1 1',
'1 1 0']


)