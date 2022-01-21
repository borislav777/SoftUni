function addItem() {

    const textInput = document.getElementById('newItemText');
    const valueInput = document.getElementById('newItemValue');
    const menu = document.getElementById('menu');
    let newOption = document.createElement('option');
    newOption.textContent = textInput.value;
    newOption.value = valueInput.value;

    menu.appendChild(newOption);
    textInput.value = '';
    valueInput.value = '';


}