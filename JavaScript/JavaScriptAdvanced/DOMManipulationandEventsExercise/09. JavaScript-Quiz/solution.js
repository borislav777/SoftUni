function solve() {
    const correctAnswer = [
        'onclick',
        'JSON.stringify()',
        'A programming API for HTML and XML documents'
    ];
    let countCorrectAnswers = 0;
    let indexSection = 0;
    document.getElementById('quizzie').addEventListener('click',onClick);
    let sections = document.querySelectorAll('#quizzie section');
    let result = document.querySelector('.results-inner h1');


    function onClick(evt){
        if (evt.target.tagName === 'P' && evt.target.className === "answer-text"){
            let answer = evt.target.textContent;
            if (correctAnswer.includes(answer)){
                countCorrectAnswers ++;
            }
            sections[indexSection].style.display = 'none';
            if (indexSection < sections.length-1){
                indexSection++;
                sections[indexSection].style.display = 'block';
            }else {
                document.getElementById('results').style.display = 'block';
                if (countCorrectAnswers === sections.length){
                    result.textContent = "You are recognized as top JavaScript fan!";
                }else {
                    result.textContent = `You have ${countCorrectAnswers} right answers`
                }

            }




        }
    }



}
