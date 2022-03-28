// use selector
const LoginForm = document.querySelector('.login-form')
const Email = document.querySelector('.email')
const Password = document.querySelector('.password')
// check reset
console.log('fe')

async function GetLoginInfo(email, password){
    let loginfo = {
        'email': email,
        'password':password
    } 
    const res = await fetch(`/common/login/api/`, {
        method: "post",
        body: JSON.stringify(loginfo),
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        } 
    })
    const data = await res.json()
    console.log(data)
}

function init(){
    LoginForm.addEventListener('submit', (e)=>{
        e.preventDefault()
        GetLoginInfo(Email.value, Password.value)
    })
}

init()
