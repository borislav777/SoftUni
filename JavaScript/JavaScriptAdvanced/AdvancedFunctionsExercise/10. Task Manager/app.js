function solve() {
    let addBtn = document.getElementById('add');
    addBtn.addEventListener('click', onAdd);
    let sections = document.querySelectorAll('section');

    function onAdd(e) {
        e.preventDefault();
        let taskName = document.getElementById('task');
        let taskDescription = document.getElementById('description');
        let dueDate = document.getElementById('date');
        if (taskName.value !== '' && taskDescription.value !== '' && dueDate.value !== '') {
            let openSection = sections[1].querySelectorAll('div')[1];
            let article = document.createElement('article');
            let header = document.createElement('h3');
            header.textContent = taskName.value;
            let descriptionP = document.createElement('p');
            descriptionP.textContent = `Description: ${taskDescription.value}`;
            let dateP = document.createElement('p');
            dateP.textContent = `Due Date: ${dueDate.value}`;
            let btnDiv = document.createElement('div');
            btnDiv.classList.add('flex');
            let startBtn = document.createElement('button');
            startBtn.textContent = 'Start';
            startBtn.classList.add('green');
            startBtn.addEventListener('click', moveInProgress)
            let deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.classList.add('red');
            deleteBtn.addEventListener('click', deleteTask)
            btnDiv.appendChild(startBtn);
            btnDiv.appendChild(deleteBtn);
            article.appendChild(header);
            article.appendChild(descriptionP);
            article.appendChild(dateP);
            article.appendChild(btnDiv);
            openSection.appendChild(article);

        }

    }

    function moveInProgress(e) {
        let deleteBtn = e.target;
        deleteBtn.textContent = 'Delete';
        deleteBtn.classList.remove('green');
        deleteBtn.classList.add('red')
        deleteBtn.addEventListener('click', deleteTask)
        let finishBtn = e.target.nextElementSibling;
        finishBtn.textContent = 'Finish';
        finishBtn.classList.remove('red');
        finishBtn.classList.add('orange')
        finishBtn.addEventListener('click', completeTask);
        let moveElement = e.target.parentElement.parentElement;


        let inProgressSection = document.getElementById('in-progress');
        inProgressSection.appendChild(moveElement);


    }

    function deleteTask(e) {
        let deleteElement = e.target.parentElement.parentElement;
        deleteElement.remove();
    }

    function completeTask(e) {

        let moveElement = e.target.parentElement.parentElement;
        let completeSection = sections[3].querySelectorAll('div')[1];
        let removeBtn = e.target.parentElement;
        moveElement.removeChild(removeBtn);

        completeSection.appendChild(moveElement);
    }
}