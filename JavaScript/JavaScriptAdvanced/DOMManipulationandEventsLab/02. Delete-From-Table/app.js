function deleteByEmail() {
    let data = Array.from(document.querySelectorAll('tbody tr'));
    let input = document.querySelector('input[name = "email"]')
    let remove = false;
    for (const el of data) {
        if (el.children[1].textContent == input.value){
            el.remove();
            
            remove = true;

        }
        
    }
    if (remove) {
        document.getElementById('result').textContent = 'Deleted';
    }else{
        document.getElementById('result').textContent = 'Not found.';
    }
}
    