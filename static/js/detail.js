const url = new URL(window.location.href)
const bookId = url.searchParams.get('id')
const Title = document.querySelector('.title')
const Content = document.querySelector('.content')
const WatchCount = document.querySelector('.watch-count')
const AuthorName = document.querySelector('.author-nickname')
const CreateDate = document.querySelector('.create_date')
const BookContent = document.querySelector('.book-content-section')

function bookContent(info){
    console.log(info)
    Title.innerHTML = `<h2>${info.data.title}</h2>`
    WatchCount.innerText = info.data.views_count
    CreateDate.innerText = info.data.create_date
    BookContent.innerText = info.data.content
}

async function getBook(id){
    const res = await fetch(`/book/book-detail/api/?id=${id}`)
    const data = await res.json()
    bookContent(data)
}

function init(){
    getBook(bookId)
}

init()