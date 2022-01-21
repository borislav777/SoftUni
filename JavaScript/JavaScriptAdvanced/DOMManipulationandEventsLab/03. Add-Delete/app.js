function addItem() {
    let field = document.getElementById('newItemText');
   let list = document.getElementById('items');
   let newField = document.createElement('li');
   newField.textContent = field.value;
   let button = document.createElement('a');
   button.textContent = '[Delete]';
   button.href = '#';
   button.addEventListener('click', removeElement);
   newField.appendChild(button);
   list.appendChild(newField);

   function removeElement(ev) {
        ev.target.parentNode.remove();
   }
}
