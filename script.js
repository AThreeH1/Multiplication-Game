document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submit');
    const feedback = document.getElementById('feedback');

    submitButton.addEventListener('click', function() {
        const answerInput = document.getElementById('answer');
        const answer = parseInt(answerInput.value);
        const num1 = parseInt(document.getElementById('num1').textContent);
        const num2 = parseInt(document.getElementById('num2').textContent);

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                answer: answer,
                num1: num1,
                num2: num2
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                feedback.textContent = 'Correct';
            } else {
                feedback.textContent = 'Wrong';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
