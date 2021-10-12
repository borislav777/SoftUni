function create(words) {
   let content = document.getElementById('content');
   for (const word of words) {
         const newDiv = document.createElement('div')
         const newParagraph = document.createElement('p');
         newParagraph.textContent = word;
         newParagraph.style.display = 'none';
         newDiv.addEventListener('click',onClick)
         newDiv.appendChild(newParagraph);
         content.appendChild(newDiv);

   }
   function  onClick(evt){

      evt.target.children[0].style.display = 'block';
   }
}