function daysMonth(month,year) {
    return new Date(year,month,0).getDate()
    
}
console.log(daysMonth(1, 2012));