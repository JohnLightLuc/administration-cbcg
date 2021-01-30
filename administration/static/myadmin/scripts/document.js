const date = document.querySelector('#date');
const printButton = document.querySelector('#print');

// SHOWS DAY //
const options = { month : 'long', day : '2-digit', year : 'numeric'};
const today = new Date();
date.innerHTML = today.toLocaleDateString('fr-FR', options);

// OPEN PRINT DIALOG BOX //
printButton.addEventListener('click', () => window.print());