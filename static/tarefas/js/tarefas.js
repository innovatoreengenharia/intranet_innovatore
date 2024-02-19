function log(message){
    console.log('> ' + message)
}



const cards = document.querySelectorAll('.card-kanban')
const dropzones = document.querySelectorAll('.dropzone')

cards.forEach(card =>{
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)

});

function dragstart(){
    dropzones.forEach(dropzone => dropzone.classList.add('highlight'))
    this.classList.add('is-dragging')
}

function drag(){

}

function dragend(){
    dropzones.forEach(dropzone => dropzone.classList.remove('highlight'))
    this.classList.remove('is-dragging')
}

//LOCAL ONDE SOLTA OS CARDS

dropzones.forEach(dropzone =>{
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)

});

function dragenter(){
}

function dragover(){
    this.classList.add('over')

    const cardBeingDragged = document.querySelector('.is-dragging')

    this.appendChild(cardBeingDragged)
}

function dragleave(){
    this.classList.remove('over')
}
function drop(){
    this.classList.remove('over')
}

// https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API