$(document).ready(function() {

  var scrollLink = $('.smoothscroll');

  // Smooth scrolling
  scrollLink.click(function(e) {
    e.preventDefault();
    $('body,html').animate({
      scrollTop: $(this.hash).offset().top
    }, 1000 );
  });

  // Active link switching
  $(window).scroll(function() {
    var scrollbarLocation = $(this).scrollTop();

    scrollLink.each(function() {

      var sectionOffset = $(this.hash).offset().top - 20;

      if ( sectionOffset <= scrollbarLocation ) {
        $(this).parent().addClass('current');
        $(this).parent().siblings().removeClass('current');
      }
    })

  })

    // navigation hide and Show
    $(window).scroll(function(){
      var scroll = $(window).scrollTop();
      if (scroll>50 && scroll<650){
        $('#nav-wrap').fadeOut('fast');
      }
      else{
        $('#nav-wrap').fadeIn('fast');
          if(scroll>645){
            $('#nav-wrap').css('background','#242628');
          }
          else{
            $('#nav-wrap').css('background','transparent');
          }
        }
    })

})
