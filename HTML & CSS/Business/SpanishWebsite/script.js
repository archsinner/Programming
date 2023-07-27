// Global variables to store the dictionaries
let englishWords = [];
let spanishWords = [];

// Function to load the word dictionaries from files
async function loadDictionaries() {
  try {
    const englishResponse = await fetch('EnglishWords.txt');
    const englishText = await englishResponse.text();
    englishWords = englishText
      .split('\n')
      .filter((word) => word.trim() !== '');

    const spanishResponse = await fetch('SpanishWords.txt');
    const spanishText = await spanishResponse.text();
    spanishWords = spanishText
      .split('\n')
      .filter((word) => word.trim() !== '');

    // Ensure both dictionaries have the same number of words
    if (englishWords.length !== spanishWords.length) {
      console.error('Error: English and Spanish dictionaries do not have the same number of words.');
    }
  } catch (error) {
    console.error('Error loading dictionaries:', error);
  }
}

// Function to translate words
function translateWord(inputWord) {
  const inputWordLC = inputWord.toLowerCase();
  const englishTranslations = getTranslations(inputWordLC, englishWords, spanishWords);
  const spanishTranslations = getTranslations(inputWordLC, spanishWords, englishWords);

  if (englishTranslations.length > 0) {
    return englishTranslations.join(', ');
  } else if (spanishTranslations.length > 0) {
    return spanishTranslations.join(', ');
  } else {
    return 'Translation not available';
  }
}

function getTranslations(word, sourceDict, targetDict) {
  const translations = [];
  for (let i = 0; i < sourceDict.length; i++) {
    if (sourceDict[i] === word) {
      const translatedWord = targetDict[i];
      if (Array.isArray(translatedWord)) {
        translations.push(...translatedWord);
      } else {
        translations.push(translatedWord);
      }
    }
  }
  return translations;
}

// Function to handle commands
function handleCommand(command) {
  const output = document.createElement('pre');
  output.innerHTML = `<span class="input">$ ${command}</span>`;

  const commandParts = command.toLowerCase().split(' ');
  const commandType = commandParts[0];

  switch (commandType) {
    case 'help':
      output.innerHTML += `<span class="output">Available commands:</span>
                           <span class="output">- list: Display a list of common Spanish words.</span>
                           <span class="output">- translate [word]: Translate the given word to Spanish.</span>`;
      break;
    case 'list':
      const spanishWordsList = spanishWords.join(', ');
      output.innerHTML += `<span class="output">Common Spanish words:</span> <span class="output">${spanishWordsList}</span>`;
      break;
    case 'translate':
      const inputWord = commandParts.slice(1).join(' ');
      if (!inputWord) {
        output.innerHTML += `<span class="output">Please provide a word to translate.</span>`;
        break;
      }

      const translatedWord = translateWord(inputWord);
      output.innerHTML += `<span class="output">${inputWord} ➜ ${translatedWord}</span>`;
      break;
    default:
      output.innerHTML += `<span class="output">Unknown command. Type 'help' for available commands.</span>`;
      break;
  }

  const terminalBody = document.querySelector('.terminal-body');
  terminalBody.appendChild(output);
  commandInput.value = '';
  commandInput.scrollIntoView();
}

// Attach the event listener to the command input
const commandInput = document.getElementById('command-input');
commandInput.addEventListener('keyup', function (event) {
  if (event.key === 'Enter') {
    const command = commandInput.value;
    handleCommand(command);
  }
});

// Load dictionaries on page load
loadDictionaries();