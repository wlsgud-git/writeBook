const form = document.querySelector('.signup-form')
const Email = document.querySelector('.email');
const Username = document.querySelector('.username');
const Nickname =  document.querySelector('.nickname')
const Password =  document.querySelector('.password')

console.log('fetch some')

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    Postsignup(Email.value, Username.value, Nickname.value, Password.value)
})

async function Postsignup(email, username, nickname, password){
    let info = {
        'email': email,
        'username': username,
        'nickname': nickname,
        'password': password
    }

    const res = await fetch(`/common/resister/`, {
        method: 'post',
        body: JSON.stringify(info),
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
    const data = await res.json()
    console.log(data)
}

function init(){

}