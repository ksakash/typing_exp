const RANDOM_QUOTE_API_URL = 'http://api.quotable.io/random'
const quoteDisplayElement = document.getElementById('quoteDisplay')
const quoteInputElement = document.getElementById('quoteInput')
const wpmElement = document.getElementById('wpm')
const errorElement = document.getElementById('error')

var current_pointer = 0
let num_mistakes = 0
let timer_start = 0
let timer_end = 0

function highLightCurrent() {
  const spanElement = quoteDisplayElement.querySelectorAll('span')[current_pointer]
  if (spanElement != null) {
    spanElement.classList.remove('correct')
    spanElement.classList.add('current')
  }
}

quoteInputElement.addEventListener('input', () => {
  const arrayQuote = quoteDisplayElement.querySelectorAll('span')
  const arrayValue = quoteInputElement.value.split('')

  let correct = true
  arrayQuote.forEach((characterSpan, index) => {
    const character = arrayValue[index]
    if (character == null) {
      characterSpan.classList.remove('correct')
      characterSpan.classList.remove('incorrect')
      correct = false
    } else if (character === characterSpan.innerText) {
      if (correct) {
        characterSpan.classList.add('correct')
        characterSpan.classList.remove('incorrect')
        characterSpan.classList.remove('current')
      }
      else {
        characterSpan.classList.remove('correct')
        characterSpan.classList.add('incorrect')
        characterSpan.classList.remove('current')
        }
      if (correct) {
        current_pointer = index + 1
      }
    } else {
      characterSpan.classList.remove('correct')
      characterSpan.classList.add('incorrect')
      characterSpan.classList.remove('current')
      correct = false
      num_mistakes += 1
    }
  })

  highLightCurrent(current_pointer)
  if (correct) {
    timer_end = getTimerTime()
    let total_time = timer_end - timer_start
    let word_length = arrayQuote.length / 5
    let wpm = (word_length * 60) / total_time
    console.log (total_time, " ", word_length, " ", wpm)
    wpmElement.innerText = wpm.toFixed(2).toString()
    errorElement.innerText = num_mistakes.toString();
    renderNewQuote()
  }
})

function getRandomQuote() {
  return fetch("/new_code")
    .then(response => response.json())
    .then(data => data.data)
}

async function renderNewQuote() {
  const quote = await getRandomQuote()
  quoteDisplayElement.innerHTML = ''
  quote.split('').forEach(character => {
    if (character === '\n') {
      const br = document.createElement('br')
      quoteDisplayElement.appendChild(br);
    }
    else if (character === '\t') {
      quoteDisplayElement.insertAdjacentHTML('beforeend', '&nbsp;&nbsp;&nbsp;&nbsp;')
    }
    else {
      const characterSpan = document.createElement('span')
      characterSpan.innerText = character
      quoteDisplayElement.appendChild(characterSpan)
    }

  })
  current_pointer = 0
  quoteInputElement.value = null
  startTimer()
  timer_start = getTimerTime()
}

let startTime
function startTimer() {
  startTime = new Date()
}

function getTimerTime() {
  return Math.floor((new Date() - startTime) / 1000)
}

wpmElement.innerText = 0
errorElement.innerText = 0
renderNewQuote()
highLightCurrent(current_pointer)
