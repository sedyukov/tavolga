const clickx= document.getElementById('pencet');
const clickx2= document.getElementById('links-hide-menu');

clickx.addEventListener('click', function(){
  clickx.classList.toggle('Diam');
  clickx2.classList.toggle('links-menu');
});


var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});