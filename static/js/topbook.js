console.log('asdasd')

async function GetTopBooks(){
    const topBook = await fetch(`/book/topbook-list/api/`)
    const topbooklist = await topBook.json()
    console.log(topbooklist)
}

function init(){
    GetTopBooks()
}

init()