async function lockedProfile() {
    const main = document.getElementById('main');
    main.replaceChildren();
    main.addEventListener('click',showMore);
    const profiles = await getProfileInfo();
    let counter = 1;
    for (const profile of Object.values(profiles)) {
        counter ++;
        const divProfile = document.createElement('div');
        divProfile.className = 'profile';
        divProfile.appendChild(newElement('img',{src:'./iconProfile2.png',className:'userIcon'}))
        divProfile.appendChild(newElement('label',{},'Lock'));
        divProfile.appendChild(newElement('input',{type:'radio',name:`user${counter}Locked`,value:'lock',checked:true}));
        divProfile.appendChild(newElement('label',{},'Unlock'));
        divProfile.appendChild(newElement('input',{type:'radio',name:`user${counter}Locked`,value:'unlock'}));
        divProfile.appendChild(newElement('br',{}));
        divProfile.appendChild(newElement('hr',{}));
        divProfile.appendChild(newElement('label',{},'Username'));
        divProfile.appendChild(newElement('input',{type:'text',name:`user${counter}Username`,value:profile.username,
            disabled:true,readOnly:true}))
        const divHiddenInfo = document.createElement('div');
        divHiddenInfo.id = `user${counter}HiddenFields`;
        divHiddenInfo.style.display = 'none';
        divHiddenInfo.appendChild(newElement('hr',{}));
        divHiddenInfo.appendChild(newElement('label',{},'Email'));
        divHiddenInfo.appendChild(newElement('input',{type:'email',name:`user${counter}Email`,value:profile.email,
            disabled:true,readOnly:true}))
        divHiddenInfo.appendChild(newElement('label',{},'Age'));
        divHiddenInfo.appendChild(newElement('input',{type:'email',name:`user${counter}Age`,value:profile.age,
            disabled:true,readOnly:true}))
        const button = document.createElement('button');
        button.textContent = 'Show more';
        divProfile.appendChild(divHiddenInfo);
        divProfile.appendChild(button);
        main.appendChild(divProfile);

    }



    async function getProfileInfo() {
        const url = 'http://localhost:3030/jsonstore/advanced/profiles';
        const result = await fetch(url);
        const data = result.json();

        return data
    }
  function showMore(e){
        if (e.target.tagName ==='BUTTON'){
            const isUnlock = e.target.parentElement.querySelector('input[value = "unlock"]').checked;
            if (isUnlock){
                if (e.target.textContent === 'Show more'){
                    e.target.previousElementSibling.style.display = 'block';
                    e.target.textContent = 'Hide it';
                }else {
                    e.target.previousElementSibling.style.display = 'none';
                    e.target.textContent = 'Show more';
                }
            }
        }
  }
}

function newElement(type, props, ...content) {
    const element = document.createElement(type);
    for (let prop in props) {
        element[prop] = props[prop];
    }
    for (let entry of content) {
        if (typeof entry == 'string' || typeof entry == 'number') {
            entry = document.createTextNode(entry);
        }
        element.appendChild(entry);
    }

    return element;
}
