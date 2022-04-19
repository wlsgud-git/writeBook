//use selector
const url = new URL(window.location)
const userMenu = document.querySelector('.nav-menu')
const Profile = document.querySelector('.user-profile')
const Options = document.querySelector('.options')
const MyProfile = document.querySelector('.user-profile')
const Menu = document.querySelector('.options')
const SearchForm = document.querySelector('.book-search-form')
const SearchInput = document.querySelector('.search-input')
//모달 관련 selector
const Modals = document.querySelector('.modals')
const Modal = document.querySelector('.modal')
const ModalX = document.querySelector('.modal-close')
const ModalForm = document.querySelector('.auth-number-form')
const ModalInput = document.querySelector('.auth-number-input')
const ModalStatus = document.querySelector('.status-mes')

// check section
console.log('ㅁ')

function countDown(minutes){
    
}

// ModalX.addEventListener('click', ()=>{
//     Modals.classList.add("none")
// })

// console.log(url)

// 검색
// SearchForm.addEventListener('submit', (e)=>{
//     e.preventDefault()
//     console.log(SearchInput.value)
// })

// menu 열었다 닫기
// function 



//쿠키 함수
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//요일 받아오는 함수
function getToday(){
    let week = ['sun','mon','tue','wed','thu','fri','sat']
    let now = new Date()
    let Today = week[now.getDay()]
    return Today
}

//count 세기 함수
function CountReduce(count){
    var s = count.toString()
    if(count < 1000){return count}

    if(count >= 1000 && count < 10000){
        return s[0] + "." + s[1] +"천"
    }
    else if(count >= 10000 && count < 100000){
        return `${s[0]}.${s[1]}만`
    }
    else if(count >= 100000 && count < 1000000){
        return `${s[0]}${s[1]}만`
    }
    else if(count >= 1000000 && count < 10000000){
        return `${s[0]}${s[1]}${s[2]}만`
    }
}

// use_variable
const csrftoken = getCookie('csrftoken');