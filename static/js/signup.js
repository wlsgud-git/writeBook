//use selector
const url = new URL(window.location)
const form = document.querySelector('.signup-form')
const Email = document.querySelector('.email');
const Username = document.querySelector('.username');
const Nickname =  document.querySelector('.nickname')
const Password =  document.querySelector('.password')

//check console
console.log('loser')

// start function 
function init(){
    form.addEventListener('submit', (e)=>{
        e.preventDefault()
        Postsignup(Email.value, Username.value, Nickname.value, Password.value)
    })
}

init()

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
    handleSigupData(data)
}

function handleSigupData(data){
    console.log(data)
    if(data.status == 200){
        alert('회원가입이 완료되었습니다')
        return window.location.href = url.origin+data.pathname
    }
    else{
        alert(data.message)
        return
    }
}