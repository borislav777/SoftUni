function solve() {

    let [check, clear] = document.querySelectorAll('button');
    let rows = document.querySelectorAll('tbody tr');
    let table = document.querySelector('table');
    let inputs = Array.from(document.querySelectorAll('#exercise tbody tr td input'));
    let output = document.querySelector('#check p');
    let minInputValue = Number(inputs[0].getAttribute('min'));
    let maxInputValue = Number(inputs[0].getAttribute('max'));
    check.addEventListener('click', validation);
    clear.addEventListener('click', clearFields)

    function validation(evt) {


        let fields = [];
        let isOKRow = true;
        let isOKCol = true;
        for (let i = 0; i < rows.length; i++) {
            let currRow = rows[i];
            let matrixRow = [];
            let inputOfCurrRow = currRow.getElementsByTagName('input');
            for (let j = 0; j < rows.length; j++) {
                let currValue = Number(inputOfCurrRow[j].value)
                matrixRow.push(currValue)
            }
            fields.push(matrixRow);


        }


        for (let col = 0; col < fields.length; col++) {
            let currCol = [];
            for (let row = 0; row < fields.length; row++) {

                currCol.push(fields[row][col]);

                let rowSet = new Set(fields[row]);
                let checkRange = fields[row].filter((n) => (n >= minInputValue && n <= maxInputValue));
                if (rowSet.size < fields.length || checkRange.length < fields.length) {
                    isOKRow = false;
                }
            }


            let colSet = new Set(currCol)
            let checkRangeCells = currCol.filter((n) => (n >= minInputValue && n <= maxInputValue));
            if (colSet.size < fields.length || checkRangeCells.length < fields.length) {
                isOKCol = false;
            }
        }


        if (isOKCol && isOKRow) {
            output.textContent = "You solve it! Congratulations!";
            table.style.border = "2px solid green";
            output.style.color = 'green';
        } else {
            output.textContent = 'NOP! You are not done yet...';
            table.style.border = "2px solid red";

            output.style.color = 'red';
        }

    }
        function clearFields(evt) {
            let fields = Array.from(document.querySelectorAll('input[type="number"]'));
            fields.forEach((f) => f.value = '')
            output.textContent = '';
            table.style.border = '';
            output.style.color = '';


        }

}



