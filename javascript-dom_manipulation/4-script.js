// Select the element with id "add_item" and the ul element with class "my_list", then append a new li element on click
const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  myList.appendChild(newLi);
});
