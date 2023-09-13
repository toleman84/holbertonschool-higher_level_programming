const request = new XMLHttpRequest();
request.open('GET', 'https://swapi-api.hbtn.io/api/films/?format=json');
request.setRequestHeader('Accept', 'application/json');
request.send();
request.addEventListener('load', function() {
    if (request.status === 200) {
        const data = JSON.parse(request.responseText);
        const movies = data.results;
        const list = document.getElementById('list_movies');
        movies.forEach(movie => {
            const listItem = document.createElement('li');
            listItem.textContent = movie.title;
            list.appendChild(listItem);
        });
    } else {
        console.error('An error occurred while fetching the data:', request.status);
    }
});
