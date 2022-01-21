function argINFO(...param) {
    let result = [];
    let pairs = {};
    param.forEach((el) => {
        let elType = typeof (el);
        pairs[elType] = pairs[elType] === undefined ? 1 : ++pairs[elType];
        result.push(`${elType}: ${el}`)
    })
    let sortedPairs = Object.keys(pairs).sort((a,b)=> pairs[a] - pairs[b]);
    sortedPairs.forEach((el)=>{
        result.push(`${el} = ${pairs[el]}`)

    })
    console.log(result.join('\n'));
}

argINFO('cat', 42, function () { console.log('Hello world!'); })