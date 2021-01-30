// ===== VARIABLE ===== //
// const wrapper = document.querySelector('#wrapper');
const form = wrapper.querySelector('#forms form');
const inputContainer = wrapper.querySelector('form > div');
const inputs = form.querySelectorAll('.input > input');

// console.log(Object.values(inputs).map(input => input.value));

// ===== FONCTIONS ===== //
function toggleActive () {
    this.classList.toggle('active');
}

function setFocus () {
    let inputCadre = this.parentNode;
    inputCadre.classList.add('focus');
}

function removeFocus (input) {
    let inputCadre = input.parentNode;
    inputCadre.classList.remove('focus');
}

function verifyInput (content) {
    console.log("Vérifié !");
}

function allInputAreFilled (e) {

    const formTitle = this.querySelector('.form-title');
    const emptyInput = Object.values(this.querySelectorAll('input'))
        .find((input) => input.value === "");
    
    if (emptyInput) {
         //Arrête l'envoi du formulaire
        e.preventDefault();
        // Crée le message d'erreur
        let p = document.createElement('p');
        p.classList.add('error');
        p.style.color = "rgb(250, 79, 79)";
        p.innerText = "Veuillez correctement remplir tous les champs !";

        if(!formTitle.nextElementSibling.matches('p.error')) {
            formTitle.insertAdjacentElement('afterend', p);
        }

        emptyInput.focus();
    }

}

// ===== EVENTS ===== //
inputs.forEach(input => input.addEventListener('focusin', setFocus));

inputs.forEach(input => input.addEventListener('focusout', function () {
    let p = document.createElement('p');
    p.classList.add('error');

    let inputCadre = input.parentNode;
    let inputValue = input.value;
    //Lorsque le champ est vide
    if (inputValue === "") {
        inputCadre.classList.add('empty');
        input.focus();
        p.innerText = "Ce champ ne doit pas être vide ! | Tous les champs sont requis";

        if(!inputCadre.nextElementSibling.matches('p.error')) {
            inputCadre.insertAdjacentElement("afterend", p);
        }
    }

    // Lorsque le champ n'est pas vide
    if (inputValue !== "") {
        inputCadre.classList.remove('empty');

        // Supprime l'erreur
        if(inputCadre.nextElementSibling.matches('p.error')) {
            let error = inputCadre.nextElementSibling;
            inputContainer.removeChild(error);
        }

        // Retirer la class focus et ajouter la class valid
        inputCadre.classList.remove('focus');
        inputCadre.classList.add('valid');
    }
}));

form.addEventListener('submit', allInputAreFilled);
