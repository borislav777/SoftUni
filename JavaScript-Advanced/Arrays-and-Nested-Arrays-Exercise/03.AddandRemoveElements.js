function addAndRemove(arr) {
    let result = [];
    let number = 1;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 'add') {
            result.push(number);
        } else {
            result.pop(number);
        }
        number++;


    }
    if (result.length > 0) {
        console.log(result.join('\n'));
    } else {
        console.log('Empty')
    }

}
addAndRemove(
    ['remove',
        'remove',
        'remove']

)