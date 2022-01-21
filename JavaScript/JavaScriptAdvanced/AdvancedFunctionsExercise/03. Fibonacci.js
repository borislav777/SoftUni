function getFibonator() {
    let prev = 1;
    let curr = 0;
    function generator() {
        let next = prev + curr;
        prev = curr;
        curr = next;
        return curr;
    }
    return generator;
}


let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib());