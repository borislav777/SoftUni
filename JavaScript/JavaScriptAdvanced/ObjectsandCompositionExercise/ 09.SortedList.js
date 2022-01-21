function createSortedList() {

    const list = {
        arr: [],
        size: 0,
        add(el) {
            list.arr.push(el);
            list.arr.sort((a, b) => a - b)
            list.size ++;
        },
        remove(i) {
            if (i>=0 && i<list.size){

            
            list.arr.splice(i,1);
            list.size --;
            }
        },
        get(i) {
            return list.arr[i];
        }
    }
    return list;
}



let list = createSortedList();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1));
list.remove(1);
console.log(list.get(1));
