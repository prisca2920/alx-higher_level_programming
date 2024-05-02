$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/?format=json', data => {
    $.each(data.results, (i, movie) => {
      const movieTitle = '<li>' + movie.title + '</li>';
      $('#list_movies').append(movieTitle);
    });
  });
});
