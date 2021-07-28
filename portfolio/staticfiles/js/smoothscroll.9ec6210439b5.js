$(document).ready(function() {

    var scrollLink = $('.smoothscroll');

    // Smooth scrolling
    scrollLink.click(function(e) {
        e.preventDefault();
        $('body,html').animate({
            scrollTop: $(this.hash).offset().top
        }, 1000);
        $('.topnav').toggleClass("open");
    });

    // // Active link switching
    // $(window).scroll(function() {
    //     var scrollbarLocation = $(this).scrollTop();

    //     scrollLink.each(function() {

    //         var sectionOffset = $(this.hash).offset().top - 20;

    //         if (sectionOffset <= scrollbarLocation) {
    //             $(this).parent().addClass('current');
    //             $(this).parent().siblings().removeClass('current');
    //         }
    //     })

    // })

    // navigation hide and Show
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 50 && scroll < 610) {
            $('#nav').fadeOut('fast');
        } else {
            $('#nav').fadeIn('fast');
            if (scroll > 610) {
                $('#nav').addClass("nav");
            } else {
                $('#nav').removeClass("nav");
            }
        }
    })

})