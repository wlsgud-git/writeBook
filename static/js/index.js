//use selector
const url = new URL(window.location)
const SlideInputs = document.querySelector('.slide-input')
const SlideContent = document.querySelector('.slide-content-img')
const SlideLeft = document.querySelector('.slide-left')
const SlideRight = document.querySelector('.slide-right')

// 슬라이드 변수값
var slideLength = 0
var slideIndex = 0
var slideNext = setInterval(slidePainter, 4000)
// check console
console.log('check')
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
            clearInterval(slideNext)
            paintSlideImg()
            paintSlideInput()
            slideNext = setInterval(slidePainter, 3000)
        })
    })

    paintSlideInput()
    paintSlideImg()
}

// 페인팅 호출하기
function slidePainter(){
    if(slideIndex == slideLength){slideIndex = 0}
    else{slideIndex +=1}
    paintSlideInput()
    paintSlideImg()
}

// 슬라이드 이미지 페인팅
function paintSlideImg(){
    const personalSlideImg = document.querySelectorAll('.slide-img')
    personalSlideImg.forEach((slideImg)=>{
        let imgNum = parseInt(slideImg.id)
        if(imgNum == slideIndex){slideImg.classList.add('img-active');slideImg.classList.remove("none")}
        else{slideImg.classList.remove('img-active');slideImg.classList.add('none')}
    })
}

// 슬라이드 이동 인풋 페인팅
function paintSlideInput(){
    const personalSlideInput = document.querySelectorAll('.slide-input-number')
    personalSlideInput.forEach((slideNum)=>{
        let inputNum = parseInt(slideNum.id)
        if(inputNum == slideIndex){slideNum.classList.add('input-active')}
        else{slideNum.classList.remove('input-active')}
    })
}

// 슬라이드 왼쪽으로
SlideLeft.addEventListener("click", ()=>{
    if(slideIndex == 0){slideIndex = slideLength}
    else{slideIndex-=1}
    clearInterval(slideNext)
    paintSlideImg()
    paintSlideInput()
    slideNext = setInterval(slidePainter, 3000)
})

// 슬라이드 오른쪽으로
SlideRight.addEventListener('click',()=>{
    if(slideIndex == slideLength){slideIndex = 0}
    else{slideIndex +=1}
    clearInterval(slideNext)
    paintSlideImg()
    paintSlideInput()
    slideNext = setInterval(slidePainter, 3000)
})

//역대 가장 인기있는 책 리스트 받아오기
































// // 요일에 맞는 책 리스트 받아오기
// async function GetDayOFBook(){
//     const DayBook = await fetch(``)
// }