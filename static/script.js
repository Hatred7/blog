const body = document.querySelectorAll('.message-body')


for (let message of body) {
    
    message.addEventListener('mouseover', () => {
        message.querySelector('.display').classList.remove('none')
    })
    message.addEventListener('mouseout', () => {
        message.querySelector('.display').classList.add('none')
    })
}



function toggleReply(pk) {
    const replayContaner = document.querySelector(`.reply-${pk}`)
    replayContaner.classList.toggle('hidden')
}