const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = document.getElementById('character');

fetch(apiUrl)
  .then((response) => {
    return response.json();
  })

  .then((data) => {
    const characterName = data.name;
    character.textContent = characterName;
  });
