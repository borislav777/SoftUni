function negativePositiveNumber(arr) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i]>=0){
            result.push(arr[i])
        }else{
            result.unshift(arr[i])
        }
        
    }
    console.log(result.join('\n'));
}
negativePositiveNumber([7, -2, 8, 9])