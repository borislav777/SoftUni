function solve() {
  let text = document.getElementById('input').value;
  let splitted = text.split('.').filter(el => el != '');
  let result = '<p>';
  let counter = 0;

  while (splitted.length > 0){
    counter ++;
    if (counter <= 3){
      result += splitted.shift() + '.';
    }else{
      result += '</p><p>';
      
      counter = 0;
    }
    
    
  }
  document.getElementById('output').innerHTML = result;
}