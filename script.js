document.querySelectorAll('input[name="mode"]').forEach(input => {
    input.addEventListener('change', function() {
        if (this.value === 'tts') {
            document.getElementById('tts-section').style.display = 'block';
            document.getElementById('stt-section').style.display = 'none';
        } else {
            document.getElementById('tts-section').style.display = 'none';
            document.getElementById('stt-section').style.display = 'block';
        }
    });
});

function convertTextToSpeech() {
    const text = document.getElementById('text-input').value;
    const lang = document.getElementById('lang-input').value;
    // Add AJAX request to send data to your Python server
}

function convertSpeechToText() {
    const audioFile = document.getElementById('audio-input').files[0];
    // Add AJAX request to send data to your Python server
}
