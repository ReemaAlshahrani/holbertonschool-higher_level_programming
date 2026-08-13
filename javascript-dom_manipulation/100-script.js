// Add, remove, and clear elements from the list when respective buttons are clicked, working from the head tag
window.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  // Add a new li element to the list
  addItem.addEventListener('click', () => {
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    myList.appendChild(newLi);
  });

  // Remove the last li element from the list if it exists
  removeItem.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      lastItem.remove();
    }
  });

  // Clear all li elements from the list
  clearList.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});
