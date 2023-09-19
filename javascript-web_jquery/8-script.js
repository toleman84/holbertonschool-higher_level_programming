// Select the UL#list_movies element using jQuery
const movieList = $('#list_movies');

// Make an AJAX request to the SWAPI API
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  method: 'GET',
  success: function(data) {
    // Get the list of movies from the JSON response
    const movies = data.results;

    // Iterate over the list of movies and add each movie title to the UL#list_movies element
    for (const movie of movies) {
      const movieTitle = movie.title;
      const listItem = $('<li></li>');
      listItem.text(movieTitle);
      movieList.append(listItem);
    }
  }
});
