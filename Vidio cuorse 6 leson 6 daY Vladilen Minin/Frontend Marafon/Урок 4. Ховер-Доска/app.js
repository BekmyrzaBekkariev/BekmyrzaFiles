const board = document.querySelector('#board')

// const colors = ['#e74c3', '#8e44ad', '#3498db', '#e67e22', '#4ecc71'] 

const colors = ['#FDD9B5', '#FBCEB1', '#7FFFD4', '#78DBE2', '#E32636', '#FF2400', '#AB274F','#8B8C7A','#FFFF99','#1CD3A2','#e74c3', '#8e44ad', '#3498db', '#e67e22', '#4ecc71'] 

// const SQUARES_NUMBER = 500
const SQUARES_NUMBER = 1000

for (let i = 0; i < SQUARES_NUMBER; i++) {
    const square = document.createElement('div')
    square.classList.add('square')

    square.addEventListener('mouseover', () => 
    setColor(square))

    square.addEventListener('mouseleave', () => 
    removeColor(square))

    board.append(square)
}

function setColor(element) {
    const color = getRandomColor()
    element.style.backgroundColor = color
    element.style.boxShadow = `0 0 2px ${color}, 0 0 10px ${color}` 
}

function removeColor(element) {
    element.style.backgroundColor = '#1d1d1d'
    element.style.boxShadow = `0 0 2px #000`
}

function getRandomColor() {
    const index = Math.floor(Math.random() * colors.length)
    return colors[index]
}