// Select the DIV#red_header element using jQuery
const redHeader = $('#red_header');

// Add a click event listener to the DIV#red_header element
redHeader.on('click', function() {
  // Select the header element using jQuery
  const header = $('header');

  // Set the text color of the header element to red
  header.css('color', '#FF0000');
});
