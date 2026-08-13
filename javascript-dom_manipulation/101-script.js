// Fetch and display translation based on the selected language code when the translate button is clicked
window.addEventListener('DOMContentLoaded', () => {
  const btnTranslate = document.querySelector('#btn_translate');
  const languageCodeSelect = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  btnTranslate.addEventListener('click', () => {
    const langCode = languageCodeSelect.value;
    if (!langCode) return; // Do nothing if no language is selected

    const url = `https://hellosalut.stefanbohacek.com/?lang=${langCode}`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching translation:', error);
      });
  });
});
