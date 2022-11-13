const RANDOM_QUOTE_API_URL = 'http://api.quotable.io/random'
const quoteDisplayElement = document.getElementById('quoteDisplay')
const quoteInputElement = document.getElementById('quoteInput')
const timerElement = document.getElementById('timer')
var current_pointer = 0

function highLightCurrent() {
  const spanElement = quoteDisplayElement.querySelectorAll('span')[current_pointer]
  if (spanElement != null) {
    spanElement.classList.remove('correct')
    spanElement.classList.remove('incorrect')
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
      characterSpan.classList.add('correct')
      characterSpan.classList.remove('incorrect')
      characterSpan.classList.remove('current')
      if (correct) {
        current_pointer = index + 1
      }
    } else {
      characterSpan.classList.remove('correct')
      characterSpan.classList.add('incorrect')
      characterSpan.classList.remove('current')
      correct = false
    }
  })

  highLightCurrent(current_pointer)

  if (correct) renderNewQuote()
})

function getRandomQuote() {
  // return "int main () {\n\treturn 0;\n}"
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
}

let startTime
function startTimer() {
  timerElement.innerText = 0
  startTime = new Date()
  setInterval(() => {
    timer.innerText = getTimerTime()
  }, 1000)
}

function getTimerTime() {
  return Math.floor((new Date() - startTime) / 1000)
}

renderNewQuote()
highLightCurrent(current_pointer)
