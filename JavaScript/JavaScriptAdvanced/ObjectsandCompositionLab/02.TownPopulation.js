function townPopulation(arr) {
    let result = {};
    for (const el of arr) {
        let [town,population] = el.split(' <-> ');
        population = Number(population);
        if (!result[town]){
            result[town] = 0;
        }
        result[town] += population;
    }
    for (const key in result) {
            console.log(`${key} : ${result[key]}`);
        }
    
}


townPopulation(
    ['Sofia <-> 1200000',
'Montana <-> 20000',
'New York <-> 10000000',
'Washington <-> 2345000',
'Las Vegas <-> 1000000']
)