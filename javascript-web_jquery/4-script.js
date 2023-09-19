// Select the DIV#toggle_header element using jQuery
const toggleHeader = $('#toggle_header');

// Add a click event listener to the DIV#toggle_header element
toggleHeader.on('click', function() {
  // Select the header element using jQuery
  const header = $('header');

  // Get the current class of the header element
  const currentClass = header.attr('class');

  // Toggle the class of the header element
  if (currentClass === 'red') {
    header.removeClass('red').addClass('green');
  } else {
    header.removeClass('green').addClass('red');
  }
});
