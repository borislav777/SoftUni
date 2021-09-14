function sumOfNumbers(a,b) {
    let n = Number(a)
    let m = Number(b)
    let result = 0;
    for (let i = n; i <= m; i++) {
        result += i
        
    }
    return result

}
console.log(sumOfNumbers('1', '5' ));
console.log(sumOfNumbers('-8', '20'));



