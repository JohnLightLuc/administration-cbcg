const updatePassword = document.querySelector('#update-password');
const updateBtn = document.querySelector('#update-btn');
const form = document.querySelector('#compte');
const newPassword = document.querySelector('#new-password');
const newPasswordTwice = document.querySelector('#new-password-twice');
const submitBtn = document.querySelector('#submit');
const updateImageBtn = document.querySelector('#update-img');
const inputFile = document.querySelector('#profileImg');
const inputsPasswordUpdated = document.querySelectorAll('#update-password input');


// FUNCTIONS //
function displayActionsBtn () {
    const actionsBtn = document.querySelector('.actions');
    actionsBtn.style.maxHeight = "100%";
}

function undisplayActionsBtn () {
    const actionsBtn = document.querySelector('.actions');
    actionsBtn.style.maxHeight = "0";
}

// Handle file
function handleFile () {
    let file = this.files[0];
    if (file) {
        previewImage(file);
        displayActionsBtn()
    }
} 

// Preview image loaded
function previewImage (file) {
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function () {
        let profileImage = document.querySelector('.cadre-img > img');
        profileImage.setAttribute('src', reader.result);
    }
}

// EVENTS //

//Show password field
updateBtn.addEventListener('click', () => {
    updatePassword.classList.toggle('active');
});

// Reset form data
form.addEventListener('reset', () => {
    updatePassword.classList.remove('active');
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

// Open input file dialog
updateImageBtn.addEventListener('click', (e) => { 
    e.preventDefault();
    inputFile.click();
});

// Change admin profile image
inputFile.addEventListener('change', handleFile, false);

// Verify if password inputs are changed
inputsPasswordUpdated.forEach(input => {
    input.addEventListener('change', () => {
        let changedInput = Object.values(inputsPasswordUpdated).find((input) => input.value != "");
        if (changedInput) {
            displayActionsBtn();
        } else {
            undisplayActionsBtn();
        }
    });
});