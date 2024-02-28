$(document).ready(function(){
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){
    if (status === "success") {
      data.results.forEach(function(movie) {
        $("#list_movies").append("<li>" + movie.title + "</li>");
      });
    } else {
      $("#list_movies").append("<li>Error: Failed to fetch movie titles</li>");
    }
  });
});
