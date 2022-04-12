const url = new URL(window.location)

function init(){
    getUserInfo()
}

init()

async function getUserInfo(){
    const userInfo = await fetch(url.pathname+"api/")
    const data = await userInfo.json()
    console.log(data)
}