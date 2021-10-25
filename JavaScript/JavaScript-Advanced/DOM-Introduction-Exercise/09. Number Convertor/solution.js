function solve() {

    let list = document.getElementById('selectMenuTo');
    let firstOption = document.createElement('option');
    let secondOption = document.createElement('option');
    firstOption.textContent = 'Binary';
    firstOption.value = 'binary';
    list.add(firstOption)
    secondOption.textContent = 'Hexadecimal';
    secondOption.value = 'hexadecimal';
    list.add(secondOption)
    document.querySelector('button').addEventListener('click', onClick);

   function onClick() {
    if (list.value ==='binary') {
        document.getElementById('result').value = Number(document.getElementById('input').value).toString(2);

    }else if (list.value === 'hexadecimal'){
        document.getElementById('result').value = Number(document.getElementById('input').value).toString(16).toUpperCase();
    }

}
}