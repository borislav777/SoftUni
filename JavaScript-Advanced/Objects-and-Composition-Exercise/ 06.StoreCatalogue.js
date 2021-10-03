function storeCatalogue(arr) {
    const catalogue = {};

    for (const product of arr) {
        let [name, price] = product.split(' : ')
        price = Number(price);
        let letterIndex = product[0];
        if (!catalogue[letterIndex]) {
            catalogue[letterIndex] = {};
        }
        catalogue[letterIndex][name] = price;
    }
    let letterSort = Object.keys(catalogue).sort((a, b) => a.localeCompare(b))
    
    for (const key of letterSort) {
       let product = Object.entries(catalogue[key]).sort((a, b) => a[0].localeCompare(b[0]))
       console.log(key);
    product.forEach((el)=>console.log(`  ${el[0]}: ${el[1]}`))
    }
}
storeCatalogue(
    ['Banana : 2',
    'Rubics Cube : 5',
    'Raspberry P : 4999',
    'Rolex : 100000',
    'Rollon : 10',
    'Rali Car : 2000000',
    'Pesho : 0.000001',
    'Barrel : 10']
)