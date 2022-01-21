window.addEventListener('load', solve);

function solve() {
    let addBtn = document.getElementById('add-btn');
    addBtn.addEventListener('click',onAdd);


    function onAdd(e){
        e.preventDefault();
        let genre = document.getElementById('genre');
        let name = document.getElementById('name');
        let author = document.getElementById('author');
        let date = document.getElementById('date');
        if (genre.value !== ''&& name.value !== '' && author.value !== ''&& date.value !== ''){
           let hitsContainer = document.querySelector('.all-hits-container');
            let div = document.createElement('div');
            div.classList.add('hits-info');
            let img = document.createElement('img');
            img.src = "./static/img/img.png";
            let h2Genre = document.createElement('h2');
            h2Genre.textContent = `Genre: ${genre.value}`;
            let h2Name = document.createElement('h2');
            h2Name.textContent = `Name: ${name.value}`;
            let h2Author = document.createElement('h2');
            h2Author.textContent = `Author: ${author.value}`;
            let h3Date = document.createElement('h3');
            h3Date.textContent = `Date: ${date.value}`;
            let saveBtn = document.createElement('button');
            saveBtn.classList.add('save-btn');
            saveBtn.textContent = 'Save song';
            saveBtn.addEventListener('click',onSave);
            let likeBtn = document.createElement('button');
            likeBtn.classList.add('like-btn');
            likeBtn.textContent = 'Like song';
            likeBtn.addEventListener('click',onLike);
            let deleteBtn = document.createElement('button');
            deleteBtn.classList.add('delete-btn');
            deleteBtn.textContent = 'Delete';
            deleteBtn.addEventListener('click',onDelete);
            div.appendChild(img);
            div.appendChild(h2Genre);
            div.appendChild(h2Name);
            div.appendChild(h2Author);
            div.appendChild(h3Date);
            div.appendChild(saveBtn);
            div.appendChild(likeBtn);
            div.appendChild(deleteBtn);
            hitsContainer.appendChild(div);
            genre.value = '';
            name.value = '';
            author.value = '';
            date.value = '';


        }


    }
    function onLike(e){
        let like = document.querySelector('.likes p');
        let currLike = Number(like.textContent.split(': ')[1]);
        currLike ++;
        like.textContent = `Total Likes: ${currLike}`;
        e.target.disabled = 'true';

    }
    function onSave(e){
        let save = document.querySelector('.saved-container');
        let savedDiv = document.querySelector('.hits-info');
        save.appendChild(savedDiv);
        savedDiv.lastElementChild.remove()
        savedDiv.lastElementChild.remove()
        let deleteBtn = savedDiv.querySelector('button');
        e.target.removeEventListener('click',onSave);
        e.target.classList.remove('save-btn')
        deleteBtn.classList.add('delete-btn');
        deleteBtn.textContent = 'Delete';
        deleteBtn.addEventListener('click',onDelete);


    }
    function onDelete(e){
        e.target.parentElement.remove();
    }
}