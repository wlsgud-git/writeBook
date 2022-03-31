console.log('fuck what')

async function GetEndBooks(){
    const res = await fetch(`/book/endbook-list/api/`)
    const data = await res.json()
    console.log(data)
}

function init(){
    GetEndBooks()
}

init()