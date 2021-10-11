function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let search = document.getElementById('searchField').value;
      let data =Array.from(document.querySelectorAll('tbody tr'));
      
      for (const el of data) {
         if (el.textContent.includes(search)) {
            el.classList.add('select')
            
         }else{
            el.classList.remove('select');
         }
      }
      document.getElementById('searchField').value = '';

   }
}