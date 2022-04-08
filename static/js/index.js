// //use selector
// const url = new URL(window.location)
// const SlideInput = document.querySelectorAll('.slide-image-input')
// const SlideContent = document.querySelector('.content-list')

// function init(){
//     GetSliderImage()
//     GetDayOFBook()
//     GetMostPopularBook()
// }

// init()

// // 슬라이드 이미지에 필요한 이미지 받아오기
// async function GetSliderImage(){
//     const sliderImage = await fetch(`/book/slide-image/api/`)
//     const data = await sliderImage.json()
//     console.log(data)
// }
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