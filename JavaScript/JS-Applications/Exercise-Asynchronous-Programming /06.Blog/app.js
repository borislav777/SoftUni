function attachEvents() {
    const loadBtn = document.getElementById('btnLoadPosts');
    loadBtn.addEventListener('click',generatePosts);
    const viewBtn = document.getElementById('btnViewPost');
    viewBtn.addEventListener('click',viewPosts);
}
async function viewPosts(e){
    const id = e.target.previousElementSibling.value;
    const [post,comments] = await Promise.all([
        getPostById(id),
        getComments(id)
    ]);


    const header = document.getElementById('post-title');
    const body = document.getElementById('post-body');
    const commentsField = document.getElementById('post-comments');
    header.textContent = post.title;
    body.textContent = post.body;
    commentsField.replaceChildren();
    for (const comment of Object.values(comments)) {
        console.log(comment)
        commentsField.appendChild(newElement('li',{id:comment.id},comment.text));
    }


}

async function generatePosts() {

    const postsField = document.getElementById('posts');
    const posts = await getAllPosts();
    for (const post of Object.values(posts)) {

        postsField.appendChild(newElement('option',{value:post.id},post.title))
    }

}
async function getPostById(id){
    const url = 'http://localhost:3030/jsonstore/blog/posts/'+ id;
    const result = await fetch(url);
    const data = await result.json();


    return data;
}

async function getAllPosts() {
    const url = 'http://localhost:3030/jsonstore/blog/posts';
    const result = await fetch(url);
    const data = await result.json();

    return data;
}

async function getComments(id) {

        const url = 'http://localhost:3030/jsonstore/blog/comments';
        const result = await fetch(url);
        const data = await result.json();
        const comments = Object.values(data).filter(el => el.postId === id);



    return comments;
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

attachEvents();