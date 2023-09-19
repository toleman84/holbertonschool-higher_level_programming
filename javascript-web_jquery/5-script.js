// Select the DIV#add_item element using jQuery
const addItem = $('#add_item');

// Add a click event listener to the DIV#add_item element
addItem.on('click', function() {
  // Create a new li element using jQuery
  const newLi = $('<li>Item</li>');

  // Append the new li element to the UL.my_list element using jQuery
  $('UL.my_list').append(newLi);
});
