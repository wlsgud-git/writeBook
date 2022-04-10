//use selector
const url = new URL(window.location)
const SlideInputs = document.querySelector('.slide-input')
const SlideContent = document.querySelector('.slide-content-img')
const SlideLeft = document.querySelector('.slide-left')
const SlideRight = document.querySelector('.slide-right')

var slideLength = 0
var slideIndex = 0
// check console
console.log('checking')

// start function
function init(){
    GetSliderImage()
    // GetDayOFBook()
    // GetMostPopularBook()
}

init()

// 슬라이드 이미지에 필요한 이미지 받아오기
async function GetSliderImage(){
    const sliderImage = await fetch(`/book/slide-image/api/`)
    const data = await sliderImage.json()
    slideLength = data.length-1

    data.forEach((data, index)=> {
        const slideInput = document.createElement('span')
        slideInput.className = "slide-input-number"
        slideInput.id = index
        SlideInputs.appendChild(slideInput)

        const slideImg = document.createElement('img')
        slideImg.className = "slide-img"
        slideImg.id = index
        slideImg.src = data.slide_image
        SlideContent.appendChild(slideImg)
    })

    const sInput = document.querySelectorAll('.slide-input-number')
    sInput.forEach((index)=>{
        index.addEventListener('click',()=>{
            let indexNum = parseInt(index.id)
            slideIndex = indexNum
            paintSlideInput()
            paintSlideImg()
        })
    })

    paintSlideInput()
    paintSlideImg()
}

function paintSlideImg(){
    const personalSlideImg = document.querySelectorAll('.slide-img')
    personalSlideImg.forEach((slideImg)=>{
        let imgNum = parseInt(slideImg.id)
        if(imgNum == slideIndex){slideImg.classList.add('img-active');slideImg.classList.remove("none")}
        else{slideImg.classList.remove('img-active');slideImg.classList.add('none')}
    })
}

function paintSlideInput(){
    const personalSlideInput = document.querySelectorAll('.slide-input-number')
    personalSlideInput.forEach((slideNum)=>{
        let inputNum = parseInt(slideNum.id)
        if(inputNum == slideIndex){slideNum.classList.add('input-active')}
        else{slideNum.classList.remove('input-active')}
    })
}

SlideLeft.addEventListener("click", ()=>{
    if(slideIndex == 0){slideIndex = slideLength}
    else{slideIndex-=1}
    paintSlideInput()
    paintSlideImg()
})

SlideRight.addEventListener('click',()=>{
    if(slideIndex == slideLength){slideIndex = 0}
    else{slideIndex +=1}
    paintSlideInput()
    paintSlideImg()
    
})


































// // 요일에 맞는 책 리스트 받아오기
// async function GetDayOFBook(){
//     const DayBook = await fetch(``)
// }
// //역대 가장 인기있는 책 리스트 받아오기
// async function GetMostPopularBook(){
//     const mostBook = await fetch(`/book/all-time-best-books/api/`)
//     const data = await mostBook.json()
//     console.log(data)
// }