async function solution() {
    const main = document.getElementById('main');
    const data = await getTitle();

    for (const title of data) {

        const divAccordion = document.createElement('div');
        divAccordion.className = 'accordion';
        const divHead = document.createElement('div');
        divHead.className = 'head';
        divHead.appendChild(newElement('span', {}, title.title));
        const button = newElement('button', {className: 'button', id: title._id}, 'More');
        button.addEventListener('click', moreInfo)
        divHead.appendChild(button);
        divAccordion.appendChild(divHead);
        main.appendChild(divAccordion);

    }
}

async function moreInfo(e) {
    const content = e.target.parentElement.parentElement;
    const id = e.target.id;
    const divExtra = newElement('div', {className: 'extra'});
    if (e.target.textContent === 'More') {
        divExtra.appendChild(newElement('p', {}, await getContent(id)));
        content.appendChild(divExtra);
        divExtra.style.display = 'block';
        e.target.textContent = 'Less';
    } else {
        document.querySelector('.extra').remove()
        e.target.textContent = 'More';
    }

}

async function getTitle() {
    const url = 'http://localhost:3030/jsonstore/advanced/articles/list';
    const result = await fetch(url);
    const data = await result.json();
    return data;
}

async function getContent(id) {
    const url = 'http://localhost:3030/jsonstore/advanced/articles/details/' + id;
    const result = await fetch(url);
    const data = await result.json();

    return data.content;
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

window.addEventListener('load', solution);
