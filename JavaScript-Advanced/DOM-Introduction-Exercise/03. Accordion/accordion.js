function toggle() {
    let btn = document.getElementsByClassName('button')[0];
    btn.textContent = btn.textContent === 'More'? 'Less': 'More';
    let text = document.getElementById('extra');
    text.style.display = text.style.display === 'none' || text.style.display === ''? 'block' : 'none';

}