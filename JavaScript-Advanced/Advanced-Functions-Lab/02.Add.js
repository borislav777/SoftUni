function solution(a){
   let num = a;
    return function  add (a){
        return num + a;
    }
}

let add5 = solution(5);
console.log(add5(2));
console.log(add5(3));