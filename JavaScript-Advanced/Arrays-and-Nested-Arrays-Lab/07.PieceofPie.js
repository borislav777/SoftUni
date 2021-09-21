function pieceOfPie(arr,firstText,secondText)  {
    return arr.slice(
        arr.indexOf(firstText),arr.indexOf(secondText)+1
    );

}
console.log(pieceOfPie(['Pumpkin Pie',
'Key Lime Pie',
'Cherry Pie',
'Lemon Meringue Pie',
'Sugar Cream Pie'],
'Key Lime Pie',
'Lemon Meringue Pie'));