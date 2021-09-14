function aggregateElements(arr){
    let sumOfNumbers = 0;
    let sumOfNumbersDivide = 0;
    let concatenateNumber = '';
    for (let i = 0; i < arr.length; i++) {
        sumOfNumbers += arr[i]
        sumOfNumbersDivide += 1/arr[i]
        concatenateNumber += String(arr[i])
        
    }
    console.log(sumOfNumbers);
    console.log(sumOfNumbersDivide);
    console.log(concatenateNumber);


}
aggregateElements([1, 2, 3])
aggregateElements([2, 4, 8, 16]
    )