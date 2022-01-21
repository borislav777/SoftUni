function solution() {
    let ingredients_quantity = {
        protein: 0,
        carbohydrate: 0,
        fat: 0,
        flavour: 0
    }
    let recipes = {
        apple: {
            carbohydrate: 1,
            flavour: 2
        },
        lemonade: {
            carbohydrate: 10,
            flavour: 20
        },
        burger: {
            carbohydrate: 5,
            flavour: 3,
            fat: 7
        },
        eggs: {
            flavour: 1,
            fat: 1,
            protein: 5
        },
        turkey: {
            flavour: 10,
            fat: 10,
            protein: 10,
            carbohydrate: 10
        }
    }
    let commands = {
        restock: function (microelement, quantity) {
            ingredients_quantity[microelement] += quantity;
            return 'Success';
        },
        prepare: function (recipe, quantity) {

            let remainingIngredient = {}
            for (const recipeKey in recipes[recipe]) {
                let remaining = ingredients_quantity[recipeKey] - recipes[recipe][recipeKey] * quantity;

                if (remaining > 0) {
                    remainingIngredient[recipeKey] = remaining;
                    Object.assign(ingredients_quantity,remainingIngredient);


                }else {
                    return `Error: not enough ${recipeKey} in stock`;
                }

            }

            return 'Success';


        },
        report() {
            return `protein=${ingredients_quantity['protein']} carbohydrate=${ingredients_quantity['carbohydrate']} fat=${ingredients_quantity['fat']} flavour=${ingredients_quantity['flavour']}`;
        }
    }

    function breakfastRobot(data) {
        if (data !== 'report') {
            let [command, cont, quantity] = data.split(' ');
            quantity = Number(quantity);
            return commands[command](cont, quantity);


        } else {
            return commands.report();
        }


    }

    return breakfastRobot;


}

let manager = solution();
console.log(manager("restock flavour 50"));
console.log(manager("prepare lemonade 4"));
console.log(manager("restock carbohydrate 10"));
console.log(manager("restock flavour 10"));
console.log(manager("prepare apple 1"));
console.log(manager("restock fat 10"));
console.log(manager("prepare burger 1"));
console.log(manager("report"));
