function lastKelement(n,k){
    let result = [];
    for (let index = 0; index < n; index++) {
        let num = 0;
        if (result.length>0){
            for (let i = result.length - k; i < result.length; i++) {
                if (i>=0){
                    num += result[i]
                }
            
            }
            result.push(num);
        }else{
            result.push(1);
        }
        
      
    }
    return result
    
}
console.log(lastKelement(8,2));