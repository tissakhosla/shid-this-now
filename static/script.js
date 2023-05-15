// JavaScript code to handle the timer buttons and form submission
var startTime, endTime, timerInterval;

function buttonAbility(startval, stopval) {
    document.getElementById('startButton').disabled = startval;
    document.getElementById('stopButton').disabled = stopval;
}

function formatTime(seconds) {
    var hours = Math.floor(seconds / 3600);
    var minutes = Math.floor((seconds % 3600) / 60);
    var remainingSeconds = Math.floor(seconds % 60);

    var formattedTime = padZero(hours) + ':' + padZero(minutes) + ':' + padZero(remainingSeconds);
    return formattedTime;
}

function padZero(value) {
    return value < 10 ? '0' + value : value;
}

function startTimer() {
    buttonAbility(true, false)
    startTime = new Date().getTime();

    displayTimer = setInterval(function () {
        var currentTime = new Date().getTime();
        var elapsedTime = (currentTime - startTime) / 1000;
        document.getElementById('timeElapsed').textContent = formatTime(elapsedTime);
    }, 100);
}

function stopTimer() {
    buttonAbility(false, true)
    endTime = new Date().getTime();
    clearInterval(displayTimer);
    logTime();
}

function logTime() {
    var textValue = document.getElementById('exercise').innerText;
    if (textValue) {
        saveToDatabase(startTime, endTime, textValue);
    }
}

function saveToDatabase(start, end, text) {
    fetch('/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text: text,
            start: start,
            end: end
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log('Data saved:', data);
        })
        .catch(error => {
            console.error('Error saving data:', error);
        });
}
