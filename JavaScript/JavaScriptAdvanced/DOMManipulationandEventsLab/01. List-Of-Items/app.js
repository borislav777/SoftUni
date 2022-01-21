function addItem() {
   let field = document.getElementById('newItemText');
   let list = document.getElementById('items');
   let newField = document.createElement('li');
   newField.textContent = field.value;
   list.appendChild(newField);

}