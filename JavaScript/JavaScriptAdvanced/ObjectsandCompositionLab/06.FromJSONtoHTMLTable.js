function fromJSON(json) {
    let inputArr = JSON.parse(json);
    let result = ['<table>'];
    result.push(addHeader(inputArr));
    inputArr.forEach((obj) => result.push(addEntry(obj)));
    result.push('</table>');


    function addHeader(arr) {
        let output = '\t<tr>';
        Object.keys(arr[0]).forEach(key => output += `<th>${convertSpecialCharacter(key)}</th>`);
        output += '</tr>';
        return output;
    }

    function addEntry(obj) {
        let output = '\t<tr>';
        Object.values(obj).forEach(value => output += `<td>${convertSpecialCharacter(value)}</td>`);
        output += '</tr>';
        return output;
    }
    

    function convertSpecialCharacter(chr) {
        return chr.toString()
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');

    }
    console.log(result.join('\n'));
}

fromJSON(
    `[{"Name":"Stamat",
    "Score":5.5},
   {"Name":"Rumen",
    "Score":6}]`
)