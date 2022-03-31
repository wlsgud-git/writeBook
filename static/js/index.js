//use selector
const Days = document.querySelectorAll('.days')
const SlideLeft = document.querySelector('.slide-left')
const SlideRight = document.querySelector('.slide-right')
//start domain
function init(){
    // 날짜마다 다른 책 리스트 보여주기
    let dday = getToday()
    history.replaceState({'day': dday}, '', `?day=${dday}`)
    GetDayBook(dday)
}
init()

// 날짜마다 다른 책 리스트 보여주기
Days.forEach((day)=>{
    day.addEventListener('click',(e)=>{
        e.preventDefault()
        let dday = e.target.id
        history.replaceState({'day': dday}, '', `?day=${dday}`)
        GetDayBook(dday)
    })
})

//요일에 맞는 책 리시트 불러오기
async function GetDayBook(day){
    const res = await fetch(`/book/day-of-book/api/?day=${day}`)
    const data = await res.json()
    console.log(data)
}