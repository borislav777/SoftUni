function solve() {
    const [genBtn, buyBtn] = document.querySelectorAll('button');
    const [input, output] = document.querySelectorAll('textarea');

    genBtn.addEventListener('click', generate);
    buyBtn.addEventListener('click', buy);
    let table = document.querySelector('tbody');

    function generate(evt) {
        const data = JSON.parse(input.value);

        for (const el of data) {

            let newRow = document.createElement('tr');
            // let imgCell = document.createElement('td')
            // let img = document.createElement('img');
            // img.src = el.img;
            // imgCell.appendChild(img)
            // let nameCell = document.createElement('td')
            // let nameP = document.createElement('p');
            // nameP.textContent = el.name;
            // nameCell.appendChild(nameP)
            // let priceCell = document.createElement('td')
            // let priceP = document.createElement('p');
            // priceP.textContent = el.price;
            // priceCell.appendChild(priceP)
            // let decCell = document.createElement('td')
            // let decP = document.createElement('p');
            // decP.textContent = el.decFactor;
            // decCell.appendChild(decP);
            // let markCell = document.createElement('td')
            // let check = document.createElement('input')
            // check.type = 'checkbox';
            // markCell.appendChild(check)
            newRow.appendChild(createCell('img',{src:el.img}));
            newRow.appendChild(createCell('p',{},el.name));
            newRow.appendChild(createCell('p',{},el.price));
            newRow.appendChild(createCell('p',{},el.decFactor));
            newRow.appendChild(createCell('input',{type: 'checkbox'}));
            table.appendChild(newRow);


        }
    }
    function createCell(nestedTag,props,content){
        let cell = document.createElement('td');
        let tag = document.createElement(nestedTag);
        for (let prop in props){
            tag[prop] = props[prop]
        }
        if (content){
            tag.textContent = content;
        }
        cell.appendChild(tag)
        return cell;

    }

    function buy(evt) {
        let markedCell = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
            .map((c) => c.parentElement.parentElement)
            .map(r => ({
                name: r.children[1].textContent,
                price: Number(r.children[2].textContent),
                decFactor: Number(r.children[3].textContent)
            }))
            .reduce((a, c, i, arr) => {
                a.names.push(c.name)
                a.total += c.price
                a.avgFactor += c.decFactor / arr.length;


                return a;

            }, {names: [], total: 0, avgFactor: 0})
        let result = `Bought furniture: ${markedCell.names.join(', ')}\n`;

        result += `Total price: ${markedCell.total.toFixed(2)}\n`;
        result += `Average decoration factor: ${markedCell.avgFactor}`;

        output.value = result;


    }


}