function notation(arr) {
    let operation = {
        '+': (first, second) => first + second,
        '-': (first, second) => first - second,
        '*': (first, second) => first * second,
        '/': (first, second) => first / second,

    }
    let numbers = [];


    while (arr.length > 0) {
        if (typeof arr[0] === 'number') {
            numbers.push(arr.shift());
        } else {
            if (numbers.length >= 2) {
                let second = numbers.pop();
                let first = numbers.pop();
                

                numbers.push(operation[arr.shift()](first, second))

            } else {

                return console.log('Error: not enough operands!');

            }
        }

    }

    if (numbers.length > 1) {
        console.log('Error: too many operands!');
    } else {
        console.log(numbers[0]);
    }

}

notation(
    [15,
        '/']
       
)