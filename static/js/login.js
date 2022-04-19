// use selector
const LoginForm = document.querySelector('.login-form')
const Email = document.querySelector('.email')
const Password = document.querySelector('.password')
// check reset
console.log('100')

function handleLoginData(data){
    console.log(data)
    if(data.status == 200){
        localStorage.setItem('access_token', data.access_token)
        window.location.href = url.origin+data.url
        alert(data.message)
        return
    }
    else{
        Password.value = ""
        alert(data.message)
        return
    }
}

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
    handleLoginData(data)
}

function init(){
    LoginForm.addEventListener('submit', (e)=>{
        e.preventDefault()
        GetLoginInfo(Email.value, Password.value)
    })
}

init()
