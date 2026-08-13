// Select the element with id "update_header" and the header element, then update header text on click
const updateHeader = document.querySelector('#update_header');
const header = document.querySelector('header');

updateHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
