function loadRepos() {
   const div = document.getElementById('res');
   let request = new XMLHttpRequest();
   request.open('GET','https://api.github.com/users/testnakov/repos',true)
   request.onload = ()=>{
      if(request.readyState === 4){
         div.textContent = request.responseText;
      }
   };
   request.send(null);

}