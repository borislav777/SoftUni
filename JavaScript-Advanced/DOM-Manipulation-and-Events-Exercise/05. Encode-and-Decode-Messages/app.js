function encodeAndDecodeMessages() {
    const encodeBtn = document.querySelectorAll('button')[0];
    encodeBtn.addEventListener('click', onEncode);
    const decodeBtn = document.querySelectorAll('button')[1];
    decodeBtn.addEventListener('click', onDecode);


    let decodeText = decodeBtn.previousElementSibling;

    function onEncode(evt) {
        let textArr = evt.target.previousElementSibling;
        let result = ''
        textArr.value.split('').forEach((el) => result += String.fromCharCode(el.charCodeAt(0) + 1))
        decodeText.value = result;
        console.log(result)
        textArr.value = '';

    }



    function onDecode(evt) {
       let result = '';
       decodeText.value.split('').forEach((el) => result += String.fromCharCode(el.charCodeAt(0) - 1))
        decodeText.value = result;
    }
}