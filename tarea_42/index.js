// Select elements here
const video = document.getElementById('video');
const playButton = document.getElementById('play');
const result = document.getElementById('result');
const comandoDiv = document.getElementById('comando');


function togglePlay() {
  if (playButton.innerText === "Start") {
    // si es la primera vez que se pulsa, el texto será start
    // y se inicia el reconocimiento y se muestran los elementos
    // escondidos
    recognition.start();
    video.style.display = "block"
    comandoDiv.style.display = "block"
  }
  // para o arranca el video
  if (video.paused || video.ended) {
    video.play();
    playButton.innerText = 'Stop'
  } else {
    video.pause();
    playButton.innerText = 'Play'

  }
}

// Añade eventlisteners alboton de start/play/pause
playButton.addEventListener('click', togglePlay);
// Oculta el video y los comandos detectados al cargar la página
video.style.display = "none"
comandoDiv.style.display = "none"




const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || window.webkitSpeechRecognitionEvent

//Parece que chorme no reconoce la gramática
const commands = ['play', 'pause'];
const grammar = '#JSGF V1.0; grammar colors; public <color> = ' + commands.join(' | ') + ' ;'

const recognition = new SpeechRecognition();
const speechRecognitionList = new SpeechGrammarList();

speechRecognitionList.addFromString(grammar, 1);

recognition.grammars = speechRecognitionList;
recognition.continuous = true;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

recognition.onresult = function (event) {
  if (event.results.length > 0) {
    let comando = event.results[event.results.length - 1][0].transcript.trim();
    if (comando === "play") {
      console.log("PLAY", comando);
      video.play();
      playButton.innerText = 'Stop'

    } else if (comando === "stop") {
      console.log("STOP", comando);
      video.pause();
      playButton.innerText = 'Play'

    } else {
      console.log("Comando no reconocido", comando);
      comando = comando + " (no soportado)"
    }
    result.innerText = comando;
    console.log(comando)
    console.log(event.results)

  }
}
recognition.onaudioend = function (event) {
  console.log('onaudioend.');

}
recognition.onspeechend = function (event) {
  console.log('onspeechend.');
  // recognition.stop();
  // recognition.start();

}
recognition.onnomatch = function (event) {
  console.log('I didnt recognise that color.');
}
recognition.onerror = function (event) {
  console.log('Error occurred in recognition: ' + event.error);

}
