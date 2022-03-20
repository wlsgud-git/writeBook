// 사용 셀렉터
let profileUsername = document.querySelector('.username-input')
let profileNickname = document.querySelector('.nickname-input')
let profileEmail = document.querySelector('.email-input')
let profileImage = document.querySelector('.img-box')
const userId = parseInt(document.querySelector('.userId').innerText)
const form = document.querySelector('.user-infomations')
//check
console.log('check1')
const ru = []
// 유저 정보 획득
async function getUser(){
    const res = await fetch(`/common/user/${userId}/api/`)
    const data = await res.json()
    ru[0] = data
    paintInput(data.username , data.nickname, data.email)
    paintImg(data.profile_image)
}
//유저 정보 변경
async function ChangeUserInfo(){
    let info = {
        'id': userId,
        'username': profileUsername.value,
        'nickname': profileNickname.value,
        'email': profileEmail.value,
    }

    const res = await fetch(`/common/user/${userId}/api/`, {
        method: "put",
        body: JSON.stringify(info),
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
    const data = await res.json()
    paintInput(data.username, data.nickname, data.email)
}

//유저 정보 표시
function paintInput(username, nickname, email){
    profileUsername.value = ""
    profileNickname.value = ""
    profileEmail.value = ""
    setTimeout(()=>{
        profileUsername.value = username
        profileNickname.value = nickname
        profileEmail.value = email  
    },1000)  
}
//유저 프로필 이미지 표시
function paintImg(img){
    setTimeout(()=>{
        profileImage.innerHTML = `<img src="${img}" alt="${img}">`
    },1000)
}

function init(){
    getUser()
    form.addEventListener('submit',(e)=>{
        e.preventDefault()

        if(profileUsername.value == ru[0].username && profileNickname.value == ru[0].nickname && profileEmail.value == ru[0].email){
            alert('변경된 정보가 없습니다')
            return
        }
        else{
            ChangeUserInfo()
        }
    })
}

init()