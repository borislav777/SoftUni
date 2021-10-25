function sameNUmbers(data) {
    let numbers = String(data);
    let same = true;
    let result = Number(numbers[0]);
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i]!== numbers[i-1]){
            same = false;
        }
        result+= Number(numbers[i])

        
    }
    console.log(same);
    console.log(result);

}
sameNUmbers(1234
    )