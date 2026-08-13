// Fetch translation from API and display it in the element with id "hello" once the DOM is fully loaded
window.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloDiv = document.querySelector('#hello');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching greeting:', error);
    });
});
