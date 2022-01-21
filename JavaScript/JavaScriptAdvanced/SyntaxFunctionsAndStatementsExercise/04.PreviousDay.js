function previousDay(year, month, day) {
    let date = new Date(year, month, day);
    date.setDate(date.getDate() -1)
    // let newDate = date.getDate().toLocaleString()
    // let newDay = newDate[0];
    // let newMonth = newDate[1];
    // let newYear = newDate[2].split(' ')[0]


    

    return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`
   


}

console.log(previousDay(2016, 10, 1));
console.log(previousDay(2016, 9, 30));