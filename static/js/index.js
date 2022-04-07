//use selector
const url = new URL(window.location)
console.log(url.searchParams.get("search-value"))
const Days = document.querySelectorAll('.days')
const SlideLeft = document.querySelector('.slide-left')
const SlideRight = document.querySelector('.slide-right')
 
// 시작 함수
function init(){
    getMostBook()
}

init()

async function getMostBook(){
    const mostBook = await fetch(`/book/all-time-best-books/api/`)
    
}
