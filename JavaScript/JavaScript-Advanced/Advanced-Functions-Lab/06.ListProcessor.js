function listProcessor(arr) {
    let result = [];
    const commands = {
        add(str) {
            result.push(str)
        },
        remove(str) {
            result = result.filter(el => el !== str)
        },
        print() {
            console.log(result.join(','))
        }
    }
    for (const data of arr) {
        let [command, str] = data.split(' ');
        commands[command](str)


    }


}

listProcessor(
    ['add pesho', 'add george', 'add peter', 'remove peter','print']
)