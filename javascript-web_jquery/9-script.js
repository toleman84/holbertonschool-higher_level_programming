// Select the DIV#hello element using jQuery
const helloDiv = $('#hello');

// Make an AJAX request to the helloSalut API
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function(data) {
    // Get the translation of "hello" from the JSON response
    const helloTranslation = data.hello;

    // Display the translation of "hello" in the DIV#hello element
    $("#hello").text(data.hello);
  }
});
