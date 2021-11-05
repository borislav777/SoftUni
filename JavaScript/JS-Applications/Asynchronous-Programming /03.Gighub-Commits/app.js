async function loadCommits() {
    const username = document.getElementById('username').value;
    const repo = document.getElementById('repo').value;
    const ul = document.getElementById('commits');
    const url = `https://api.github.com/repos/${username}/${repo}/commits`;
    ul.textContent = 'Loading....'
    ul.replaceChildren()
    try {
        const result = await fetch(url);
        if (result.ok === false){
            throw new Error(`Error: ${result.status} (Not Found)`)
        }
        const data = await result.json();

        data.forEach(el=>{

            let li = document.createElement('li')
            li.textContent = `${el.commit.committer.name}: ${el.commit.message}`;
            ul.appendChild(li)
        })
    }catch (error){
        let li = document.createElement('li')
        li.textContent = error.message;
        ul.appendChild(li);
    }

}