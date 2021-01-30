// VARIABLES //

const wrapper = document.querySelector('#wrapper');
const dropdowns = document.querySelectorAll('.dropdown');
const date = document.querySelector('#date');


// SHOWS DAY //
const options = {weekday : 'long', month : 'long', day : '2-digit', year : 'numeric'};
const today = new Date();
date.innerHTML = today.toLocaleDateString('fr-FR', options);

// EVENTS //

dropdowns.forEach((dropdown) => dropdown.addEventListener('click', function(e) {
    e.stopPropagation();
    let activeDropdown = Object.values(dropdowns).find((dropdownActive) => dropdownActive.classList.contains('active'));

    if(activeDropdown && activeDropdown !== dropdown) {
        activeDropdown.classList.remove('active');
    }
    dropdown.classList.toggle('active');
}));

window.addEventListener('click', function(e) {
    e.stopPropagation();
    dropdowns.forEach((dropdown) => {
        if (dropdown.classList.contains('active')) {
            dropdown.classList.remove('active');
        }
    });
});

