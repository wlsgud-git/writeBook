let profileUsername = document.querySelector('.username-input')
let profileNickname = document.querySelector('.nickname-input')
let profileEmail = document.querySelector('.email-input')
const userId = parseInt(document.querySelector('.userId').innerText)
console.log('fuck sibal')

async function getUser(){
    const res = await fetch(`/common/user/${userId}/api/`)
    const data = await res.json()
    paintInput(data.username , data.nickname, data.email)
}

function paintInput(username, nickname, email){
    profileUsername.value = username
    profileNickname.value = nickname
    profileEmail.value = email    
}

function init(){
    getUser()
}

init()