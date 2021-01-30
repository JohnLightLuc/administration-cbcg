// ===== VARIABLE ===== //
const wrapper = document.querySelector('#wrapper');
const dropdown = wrapper.querySelector('.dropdown');

// ===== FONCTIONS ===== //
function toggleActive () {
    this.classList.toggle('active');
}

// ===== EVENTS ===== //
dropdown.addEventListener('click', toggleActive);