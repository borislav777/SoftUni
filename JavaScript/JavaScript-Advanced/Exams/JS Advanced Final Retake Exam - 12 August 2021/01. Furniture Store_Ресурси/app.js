window.addEventListener('load', solve);

function solve() {
    const addBtn = document.getElementById('add');
    addBtn.addEventListener('click', onAdd);

    function onAdd(e) {
        e.preventDefault();
        let modelFiled = document.getElementById('model');
        let yearFiled = document.getElementById('year');
        let descriptionFiled = document.getElementById('description');
        let priceFiled = document.getElementById('price');
        const year = yearFiled.value
        const price = priceFiled.value
        if (modelFiled.value !== '' && descriptionFiled.value !== '' && year > 0 && price > 0) {
            let furnitureList = document.getElementById('furniture-list');
            let tr = document.createElement('tr');
            tr.classList.add('info');
            let tdModel = document.createElement('td');
            tdModel.textContent = modelFiled.value;
            let tdPrice = document.createElement('td');
            tdPrice.textContent = Number(priceFiled.value).toFixed(2);
            let tdBtn = document.createElement('td');
            let moreInfoBtn = document.createElement('button');
            moreInfoBtn.classList.add('moreBtn');
            moreInfoBtn.textContent = 'More Info';
            moreInfoBtn.addEventListener('click', moreInfo)
            let buyBtn = document.createElement('button');
            buyBtn.classList.add('buyBtn');
            buyBtn.textContent = 'Buy it';
            buyBtn.addEventListener('click', buy)
            let trHide = document.createElement('tr');
            trHide.classList.add('hide');
            let tdYear = document.createElement('td');
            tdYear.textContent = `Year: ${yearFiled.value}`;
            let tdDescription = document.createElement('td');
            tdDescription.colSpan = 3;
            tdDescription.textContent = `Description: ${descriptionFiled.value}`;
            trHide.appendChild(tdYear);
            trHide.appendChild(tdDescription);
            tdBtn.appendChild(moreInfoBtn);
            tdBtn.appendChild(buyBtn);
            tr.appendChild(tdModel);
            tr.appendChild(tdPrice);
            tr.appendChild(tdBtn);
            furnitureList.appendChild(tr);
            furnitureList.appendChild(trHide);
            modelFiled.value = '';
            yearFiled.value = '';
            descriptionFiled.value = '';
            priceFiled.value = '';


        }

    }

    function moreInfo(e) {

        let hideField = e.target.parentElement.parentElement.nextElementSibling;

        if (e.target.textContent === 'More Info') {

            e.target.textContent = 'Less Info';
            hideField.style.display = 'contents';
        } else {

            e.target.textContent = 'More Info';
            hideField.style.display = 'none';
        }


    }

    function buy(e) {
        let total = document.querySelector('.total-price');
        let currRow = e.target.parentElement.parentElement;
        let hideRow = currRow.nextElementSibling;
        let price = Number(e.target.parentElement.previousElementSibling.textContent);
        total.textContent = (Number(total.textContent) + price).toFixed(2)
        hideRow.remove()
        currRow.remove();


    }
}
