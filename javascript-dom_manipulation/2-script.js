// Select the element with id "red_header" and the header element, then add the 'red' class on click
const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', () => {
  header.classList.add('red');
});
