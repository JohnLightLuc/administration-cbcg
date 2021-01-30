
const updatePasswordBtn = document.querySelector('#update-btn');
const updateYearBtn = document.querySelector('#update-year');
const updateBtns = document.querySelectorAll('.current-info .btn');
const form = document.querySelector('#compte');
const submitBtn = document.querySelector('#submit');
const inputYear = document.querySelector('.sub-input #annee-service');
const updatePassword = document.querySelector('#update-password');
const newPassword = document.querySelector('#new-password');
const newPasswordTwice = document.querySelector('#new-password-twice');const date = document.querySelector('#date');



// SHOWS DAY //
const options = {weekday : 'long', month : 'long', day : '2-digit', year : 'numeric'};
const today = new Date();
date.innerHTML = today.toLocaleDateString('fr-FR', options);


// FUNCTIONS //
function displayActionsBtn () {
    const actionsBtn = document.querySelector('.actions');
    actionsBtn.style.maxHeight = "100%";
}

function undisplayActionsBtn () {
    const actionsBtn = document.querySelector('.actions');
    actionsBtn.style.maxHeight = "0";
}

// EVENTS //

//Show password field
updateBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        let job = btn.getAttribute('job');
        if (job === 'year') inputYear.classList.toggle('active');
        if (job === 'password') updatePassword.classList.toggle('active');
        displayActionsBtn();
    }, false)
});

// Reset form data
form.addEventListener('reset', () => {
    updatePassword.classList.remove('active');
    inputYear.classList.remove('active');
    newPasswordTwice.classList.remove('valid');
    newPasswordTwice.classList.remove('no-valid');
});

// Verify password entries
newPasswordTwice.addEventListener('change', () => {
    let newPasswordValue = newPassword.value;
    let newPasswordTwiceValue = newPasswordTwice.value;

    if (newPasswordTwiceValue === "" || newPasswordTwiceValue !== newPasswordValue) {
        newPasswordTwice.classList.add('no-valid');
        submitBtn.setAttribute('disabled', 'disabled');
    } else {
        newPasswordTwice.classList.remove('no-valid');
        newPasswordTwice.classList.add('valid');
        submitBtn.removeAttribute('disabled');
    }
});