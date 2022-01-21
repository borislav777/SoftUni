function lockedProfile() {
    document.getElementById('main').addEventListener('click', onClick);

    function onClick(evt) {
        if (evt.target.tagName === 'BUTTON') {
            let isUnlock = evt.target.parentElement.querySelector('input[value = "unlock"]').checked;
            if (isUnlock) {
                if (evt.target.textContent === 'Show more') {
                    evt.target.previousElementSibling.style.display = 'block';
                    evt.target.textContent = 'Hide it';
                } else {
                    evt.target.previousElementSibling.style.display = '';
                    evt.target.textContent = 'Show more';
                }
            }
        }
    }

}