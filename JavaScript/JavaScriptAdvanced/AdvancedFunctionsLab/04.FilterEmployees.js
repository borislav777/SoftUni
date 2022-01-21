function employeeFilter(data,criteria){
    let employees = JSON.parse(data);

    if (criteria === 'All'){
        for (let i = 0; i < employees.length; i++) {
            console.log(`${i}. ${employees[i].first_name} ${employees[i].last_name} - ${employees[i].email}}`)
        }
    } else {
        let [prop,value] = criteria.split('-')
        let filteredArray = employees.filter(v=>v[prop] === value)
        for (let i = 0; i < filteredArray.length; i++) {
            console.log(`${i}. ${filteredArray[i].first_name} ${filteredArray[i].last_name} - ${filteredArray[i].email}`)
        }

    }
}
employeeFilter(
    `[{
    "id": "1",
    "first_name": "Kaylee",
    "last_name": "Johnson",
    "email": "k0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Johnson",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  }, {
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }, {
    "id": "4",
    "first_name": "Evanne",
    "last_name": "Johnson",
    "email": "ev2@hostgator.com",
    "gender": "Male"
  }]`,
    'last_name-Johnson'

)