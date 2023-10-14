let BtnClick = document.getElementById('BtnClick');
let dataContainer = document.getElementById('data');
let element = document.getElementsByClassName("container");
let h1 = document.getElementById("h1");

function myFunc(event, tabName) {
    data = document.getElementsByClassName("data");
    for (i = 0; i < data.length; i++) {
        data[i].style.display = "none";
    }
    tabs = document.getElementsByClassName("tabs");
    for (i = 0; i < tabs.length; i++) {
        tabs[i].className = tabs[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}