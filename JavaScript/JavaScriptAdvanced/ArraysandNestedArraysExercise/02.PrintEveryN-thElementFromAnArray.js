function nThElement(arr,number) {

    let result = arr.filter((num,i)=>{
        return i % number === 0;
    })
    return result
}
nThElement(
    ['5',
        '20',
        '31',
        '4',
        '20'],
    2
)