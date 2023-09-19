// Select the DIV#update_header element using jQuery
const updateHeader = $('#update_header');

// Add a click event listener to the DIV#update_header element
updateHeader.on('click', function() {
  // Select the header element using jQuery
  const header = $('header');

  // Update the text of the header element
  header.text('New Header!!!');
});
