function solve() {
  let text = document.getElementById('text').value.split(' ');
  let convention = document.getElementById('naming-convention').value;
  let result = '';
  if (convention == 'Camel Case'){
    result += text[0].toLowerCase();
    for (let i = 1; i < text.length; i++) {
      result += text[i][0].toUpperCase() + text[i].slice(1).toLowerCase();
      
    }
      
  }else if (convention == 'Pascal Case'){
    for (let i = 0; i < text.length; i++) {
      result += text[i][0].toUpperCase() + text[i].slice(1).toLowerCase();
      
    }
  }else{
    result = 'Error!'
  }
  document.getElementById('result').textContent = result;

 
}