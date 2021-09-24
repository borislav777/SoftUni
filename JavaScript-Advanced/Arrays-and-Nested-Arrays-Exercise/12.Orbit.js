function orbit(arr) {
    let width = arr[0];
    let height = arr[1];
    let x = arr[2];
    let y = arr[3];
    let matrix = new Array(height);


    for (let i = 0; i < width; i++) {
        matrix[i] = new Array(width);

    }
    matrix[x][y] = 1;
    for (let r = 0; r < width; r++) {
        for (let c = 0; c < height; c++) {
            matrix[r][c] = Math.max(Math.max(Math.abs(x - r), Math.abs(y - c))) + 1;
        }

    }
    console.log(matrix.map((trim)=>trim.join(' ')).join('\n'));


}
orbit([4, 4, 0, 0])