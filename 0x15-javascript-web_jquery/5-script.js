$('DIV#add_item').click(function () {
  const newItem = $('<li>').text('Item');
  $('UL.my_list').append(newItem);
});
