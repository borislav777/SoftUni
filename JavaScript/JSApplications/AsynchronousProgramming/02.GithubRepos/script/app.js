function loadRepos() {
	const userName = document.getElementById('username').value;
	const ul = document.querySelector('ul');
	ul.innerHTML = '';
	fetch(`https://api.github.com/users/${userName}/repos`)
		.then(r=> {
			if(r.status !== 200){
				throw new Error(`${r.status} ${r.statusText}`)
			}
			return r.json()
		})

		.then(data=>{


			console.log(data)
			for (const element of data) {
				let li = document.createElement('li')

				let a = document.createElement('a');
				a.textContent = element.full_name;
				a.href = element.html_url;
				li.appendChild(a);
				ul.appendChild(li);
			}

		})
		.catch(error=> {
			let li = document.createElement('li')
			li.textContent = error.message;
			ul.appendChild(li);
		})
}
