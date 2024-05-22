const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movies = document.getElementById('list_movies');

fetch(apiUrl)
    .then((response) => {
        return response.json();
    })

    .then((data) => {
        list_movie = data.results;

        for (let i = 0; i < list_movie.length; i++) {
            const movie = document.createElement('li');
            movies.appendChild(movie);
            movie.textContent = list_movie[i].title;

        };

    });
