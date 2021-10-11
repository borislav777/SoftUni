function focused() {
    const fields = document.getElementsByTagName('input');

    for (const field of fields) {
        field.addEventListener('focus',onFocus);
        field.addEventListener('blur',onBlur)
    }

    function  onFocus(evt){
        evt.target.parentNode.classList.add('focused')
    }

    function onBlur(evt){
        evt.target.parentNode.classList.remove('focused')
    }
}