// Select the element with id "red_header" and the header element, then change header color on click
const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', () => {
  header.style.color = '#FF0000';
});
