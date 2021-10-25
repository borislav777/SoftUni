function solve() {

    let onScreenBtn = document.querySelector('#container button')
    onScreenBtn.addEventListener('click', onScreen)
    let clearBtn = document.querySelectorAll('button')[1];
    clearBtn.addEventListener('click', onClear);


    function onScreen(e) {
        e.preventDefault();
        let movieName = document.querySelector('input[placeholder="Name"]');
        let movieHall = document.querySelector('input[placeholder="Hall"]');
        let ticketPrice = document.querySelector('input[placeholder="Ticket Price"]');
        let movieOnScreen = document.querySelector('#movies ul')
        if (movieName.value !== '' && movieHall.value !== '' && ticketPrice.value !== '' && !isNaN(Number(ticketPrice.value))) {
            let newMovie = document.createElement('li');
            let span = document.createElement('span');
            span.textContent = movieName.value;
            let strong = document.createElement('strong');
            strong.textContent = `Hall: ${movieHall.value}`;
            let div = document.createElement('div');
            let priceStrong = document.createElement('strong');
            priceStrong.textContent = Number(ticketPrice.value).toFixed(2);
            let input = document.createElement('input');
            input.placeholder = 'Tickets Sold';
            let archiveBtn = document.createElement('button');
            archiveBtn.addEventListener('click', onArchive);
            archiveBtn.textContent = 'Archive';
            div.appendChild(priceStrong);
            div.appendChild(input);
            div.appendChild(archiveBtn);
            newMovie.appendChild(span);
            newMovie.appendChild(strong);
            newMovie.appendChild(div);
            movieOnScreen.appendChild(newMovie);
            movieName.value = '';
            movieHall.value = '';
            ticketPrice.value = '';

        }
    }

    function onArchive(e) {
        let data = e.target.parentElement.parentElement;
        let field = data.querySelector('div input')

        if (field.value !== '' && !isNaN(Number(field.value))) {
            let movieArchive = document.querySelector('#archive ul')
            let archiveLi = document.createElement('li');
            let archivedMovieName = data.querySelector('span')
            let archiveSpan = document.createElement('span');
            archiveSpan.textContent = archivedMovieName.textContent;
            let archiveStrong = document.createElement('strong');
            let price = data.querySelector('div strong')
            let totalAmount = Number(field.value) * Number(price.textContent);
            archiveStrong.textContent = `Total amount: ${totalAmount.toFixed(2)}`;
            let deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.addEventListener('click', onDelete);
            archiveLi.appendChild(archiveSpan);
            archiveLi.appendChild(archiveStrong);
            archiveLi.appendChild(deleteBtn);
            movieArchive.appendChild(archiveLi)
            data.remove()


        }
    }

    function onDelete(e) {
        let currList = e.target.parentElement
        currList.remove();
    }

    function onClear(e) {
        let archive = Array.from(document.querySelectorAll('#archive ul li'));
        archive.forEach((el) => el.remove());

    }


}