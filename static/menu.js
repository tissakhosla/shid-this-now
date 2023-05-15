document.addEventListener('DOMContentLoaded', function () {
    var icon = document.querySelector('.hamburger');
    var menu = document.querySelector('.menu');

    icon.addEventListener('click', function () {
        this.classList.toggle('open');
        menu.classList.toggle('open');
    });

});