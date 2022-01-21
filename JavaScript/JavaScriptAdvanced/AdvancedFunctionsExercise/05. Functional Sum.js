function add(a) {
    let num = 0;

    function sum(a) {
        num += a;
        return sum;
    }

    sum.toString = () => {
        return num;
    }
    return sum(a);


}

console.log(add(1)(6)(-3).toString())
