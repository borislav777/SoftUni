function fruit(typeFruit,weight,price) {
    let gramsToKg = weight / 1000
    let totalSum = gramsToKg * price

    console.log(`I need $${totalSum.toFixed(2)} to buy ${gramsToKg.toFixed(2)} kilograms ${typeFruit}.`);
}
fruit('orange', 2500, 1.80)
fruit('apple', 1563, 2.35)
