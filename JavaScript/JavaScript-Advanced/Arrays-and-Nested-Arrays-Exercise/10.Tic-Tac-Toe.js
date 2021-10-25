function ticTacToe(moves) {

    function isWinner(p, f) {
        let regex = new RegExp(p, 'g');
        let firstRow = [f[0][0], f[0][1], f[0][2]].filter((v) => v === p).length;
        let secondRow = [f[1][0], f[1][1], f[1][2]].filter((v) => v === p).length;
        let thirdRow = [f[2][0], f[2][1], f[2][2]].filter((v) => v === p).length;
        let firstCol = [f[0][0], f[1][0], f[2][0]].filter((v) => v === p).length;
        let secondCol = [f[0][1], f[1][1], f[2][1]].filter((v) => v === p).length;
        let thirdCol = [f[0][2], f[1][2], f[2][2]].filter((v) => v === p).length;
        let firstDiagonal = [f[0][0], f[1][1], f[2][2]].filter((v) => v === p).length;
        let secondDiagonal = [f[2][0], f[1][1], f[0][2]].filter((v) => v === p).length;

        if (firstRow === f.length || secondRow === f.length || thirdRow === f.length || firstCol === f.length || secondCol === f.length || thirdCol === f.length || firstDiagonal === f.length || secondDiagonal === f.length) {
            return true;
        }
        return false;






    }
    let field = [
        [false, false, false],
        [false, false, false],
        [false, false, false]
    ]
    let player = 'X';
    let isWin = false;
    let turns = 0;
    for (let i = 0; i < moves.length; i++) {
        let [row, col] = moves[i].split(' ');

        if (field[row][col] !== false) {
            console.log("This place is already taken. Please choose another!");

        } else {

            field[row][col] = player;
            turns++;
            if (isWinner(player, field)) {

                isWin = true;
                break;
            } else if (turns === 9) {
                break;
            }
            player = player == 'X' ? 'O' : 'X';
        }
        

    }
    if (isWin) {
        console.log(`Player ${player} wins!`);
    } else {
        console.log("The game ended! Nobody wins :(");
    }
    for (const row of field) {
        console.log(row.join('\t'));
    }
    

}

ticTacToe(
    ["0 0",
        "0 0",
        "1 1",
        "0 1",
        "1 2",
        "0 2",
        "2 2",
        "1 2",
        "2 2",
        "2 1"]

)