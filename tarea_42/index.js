// Select elements here
const video = document.getElementById('video');
const playButton = document.getElementById('play');
const stopButton = document.getElementById('stop');
const result = document.getElementById('result');
const testButton = document.getElementById('test-button');

function togglePlay() {
    if (video.paused || video.ended) {
      video.play();
    } else {
      video.pause();
    }
  }

  // Add eventlisteners here
playButton.addEventListener('click', togglePlay);




const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || window.webkitSpeechRecognitionEvent

//Parece que chorme no reconoce la gramática
const commands = [ 'play' , 'pause' ];
const grammar = '#JSGF V1.0; grammar colors; public <color> = ' + commands.join(' | ') + ' ;'

const recognition = new SpeechRecognition();
const speechRecognitionList = new SpeechGrammarList();

speechRecognitionList.addFromString(grammar, 1);

recognition.grammars = speechRecognitionList;
recognition.continuous = true;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

  recognition.onresult = function(event) {
    if (event.results.length > 0) {
        const comando = event.results[event.results.length-1][0].transcript.trim();
        if (comando === "play"){
            console.log("PLAY",comando);
            video.play();
        } else if (comando === "stop") {
            console.log("STOP",comando);
            video.pause();
        } else {
            console.log("Comando no reconocido",comando);
        }
        result.innerText = comando;
        console.log(comando)
        console.log(event.results)

    }
  }
  recognition.onaudioend = function(event) {
    console.log( 'onaudioend.');
   
  }
  recognition.onspeechend = function(event) {
    console.log( 'onspeechend.');
  
  }
  recognition.onnomatch = function(event) {
    console.log( 'I didnt recognise that color.');
  }
  recognition.onerror = function(event) {
    console.log( 'Error occurred in recognition: ' + event.error);

  }
  testButton.addEventListener('click', recognition.start());