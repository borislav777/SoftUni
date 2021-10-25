window.addEventListener('load', solution);

function solution() {
  const submitBtn = document.getElementById('submitBTN');
  submitBtn.addEventListener('click',submit);
  const continueBtn = document.getElementById('continueBTN');
  continueBtn.disabled = true;
  const editBtn = document.getElementById('editBTN');
  editBtn.disabled = true;
  const fullNameField = document.getElementById('fname');
  const emailField = document.getElementById('email');
  const phoneNumberField = document.getElementById('phone');
  const addressField = document.getElementById('address');
  const postalCodeField = document.getElementById('code');

  function submit(e){
    e.preventDefault();
    let fullName = fullNameField.value;
    let email= emailField.value;
    let phone = phoneNumberField.value;
    let address = addressField.value;
    let postalCode = postalCodeField.value;

    if (fullNameField.value !== '' && emailField.value !== ''){
      let information = document.getElementById('infoPreview');
      information.appendChild(el('li',`Full Name: ${fullName}`));
      information.appendChild(el('li',`Email: ${email}`));
      information.appendChild(el('li',`Phone Number: ${phone}`));
      information.appendChild(el('li',`Address: ${address}`));
      information.appendChild(el('li',`Postal Code: ${postalCode}`));
      const clearField = Array.from(document.getElementById('form').querySelectorAll("input"));
      clearField.forEach(el=> {
        if (el.type !== 'button'){
          el.value = '';
        }
      });

      continueBtn.addEventListener('click',onContinue);
      e.target.disabled = true;

      editBtn.disabled = false;
      continueBtn.disabled = false;
      editBtn.addEventListener('click',(e)=>{

        let data = Array.from(e.target.parentElement.parentElement.querySelectorAll('li'));
        fullNameField.value = fullName;
        emailField.value = email;
        phoneNumberField.value = phone;
        addressField.value = address;
        postalCodeField.value = postalCode;
        submitBtn.disabled = false;
        for (const li of data) {
          li.remove();
        }
        editBtn.disabled = true;
        continueBtn.disabled = true;
      })

    }

  }

  function onContinue(e) {
    const block = document.getElementById('block');
    while (block.firstChild){
      block.firstChild.remove()
    }
    let message = document.createElement('h3');
    message.textContent = 'Thank you for your reservation!';
    block.appendChild(message);

  }
  function el(type,...content) {
    const element = document.createElement(type);


    for (let entry of content) {
      if (typeof entry == 'string' || typeof entry == 'number') {
        entry = document.createTextNode(entry);
      }
      element.appendChild(entry);
    }

    return element;
  }


}
