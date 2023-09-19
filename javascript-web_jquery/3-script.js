// Select the DIV#red_header element using jQuery
const redHeader = $('#red_header');

// Add a click event listener to the DIV#red_header element
redHeader.on('click', function() {
  // Select the header element using jQuery
  const header = $('header');

  // Add the class red to the header element
  header.addClass('red');
});
