function validate() {
    let input = document.getElementById('email');
    input.addEventListener('change',onChange);

    function  onChange(evt){
        let pattern = /[a-z]+@[a-z]+\.[a-z]+$/;

        if (pattern.test(evt.target.value)){
            evt.target.classList.remove('error');

        }else {
            evt.target.classList.add('error');
        }
    }
}