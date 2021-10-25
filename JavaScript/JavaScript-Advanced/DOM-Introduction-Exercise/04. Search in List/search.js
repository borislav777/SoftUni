function search() {
   let towns = Array.from(document.querySelectorAll('ul li'));
   let search = document.getElementById('searchText').value;
   let counter = 0;
   for (const el of towns) {
      if (el.textContent.includes(search)&& search) {
         el.style.fontWeight = 'bold';
         el.style.textDecoration = 'underline';
         counter ++;

      }else{
         el.style.fontWeight = 'normal';
      el.style.textDecoration = '';
      }
      
   }
   document.getElementById('result').textContent =  `${counter} matches found`;
   
}
