function cars(data) {
    let newCars = {}
    const commands = {
        create(name, ...param) {
            if (param.length > 0) {
                let parentName = param[1];
                newCars[name] = Object.create(newCars[parentName])
            } else {
                newCars[name] = {};
            }

        },

        set(name, ...param) {
            let [key, value] = param;
            newCars[name][key] = value;
        },

        print(name, ...param) {
            let result = [];
            for (const key in newCars[name]) {
                result.push(`${key}:${newCars[name][key]}`)
            }
            console.log(result.join(','))
        }
    }

    for (const el of data) {
        let [command, name, ...other] = el.split(' ');
        commands[command](name, ...other)
    }

}

cars(
    ['create c1',
        'create c2 inherit c1',
        'set c1 color red',
        'set c2 model new',
        'print c1',
        'print c2']
)