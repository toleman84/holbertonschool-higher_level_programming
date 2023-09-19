// Select the DIV#character element using jQuery
const characterDiv = $('#character');

// Make an AJAX request to the SWAPI API
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  method: 'GET',
  success: function(data) {
    // Get the character name from the JSON response
    const characterName = data.name;

    // Display the character name in the DIV#character element
    characterDiv.text(characterName);
  }
});
