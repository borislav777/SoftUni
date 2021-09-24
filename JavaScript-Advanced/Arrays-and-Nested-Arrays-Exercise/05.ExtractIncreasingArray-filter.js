function extract(arr) {
    let biggestNumber = Number.MIN_SAFE_INTEGER;
    let result = arr.filter((v)=>{
        if (v >= biggestNumber){
            biggestNumber = v;
            return true;
        }
        return false;
        
    })
    return result;
}
console.log(extract(
    [1, 
        3, 
        8, 
        4, 
        10, 
        12, 
        3, 
        2, 
        24]
));

console.log(extract(
    [1, 
        2, 
        3,
        4]
))
console.log(extract(
    []
        
))
