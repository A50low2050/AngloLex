var btn = document.getElementsByClassName('dropdown-item');
var elem = document.getElementsByClassName('span__item');


var storedValue = localStorage.getItem('sort')


btn[1].onclick = function() {
    localStorage.setItem('sort', 'alphabetically');
}

btn[2].onclick = function() {
    localStorage.setItem('sort', 'recent_saving');
}


if (storedValue == null) {
    localStorage.setItem('sort', 'recent_saving')
} else if (storedValue == 'alphabetically'){
    btn[0].classList.add('active');
    elem[0].classList.add('active');

} else if (storedValue == 'recent_saving'){
    btn[2].classList.add('active');
    elem[1].classList.add('active');
}