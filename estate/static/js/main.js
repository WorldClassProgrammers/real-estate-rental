const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

 // it used jquerry function to look for id=message and will auto fadeout
setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 3000);
