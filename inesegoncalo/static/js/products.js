window.addEventListener('load',onload);
window.addEventListener('scroll', checkContentDivs,false);

function fillValueBars(){
    const elements = document.getElementsByClassName("value_bar");
    for (const element of elements){
        const value = Number(element.getAttribute('value')) || 0;
        element.style.width = Math.max(0, Math.min(100, value)) + "%";
    }
}

function checkContentDivs() {
    var contentDivs = document.querySelectorAll(".productSliddingDivs");
    var triggerHeight = window.innerHeight * 8/10;

    contentDivs.forEach(function(div) {
        var divTop = div.getBoundingClientRect().top;
        if (divTop < triggerHeight) {
            div.classList.add('show');
        } else {
            div.classList.remove('show');
        }
    });
}

function changeWindowStyle(){
    let window = document.getElementsByTagName('body')[0];
    window.style = 'height: auto!important;overflow-x: hidden!important;'
}

function onload(){
    changeWindowStyle();
    fillValueBars();
    checkContentDivs();
}