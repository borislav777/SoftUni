function colorize() {
   let colorElements = document.querySelectorAll('table tr:nth-child(even)');
   for (const el of colorElements) {
       el.style.backgroundColor = 'teal';
   }
}