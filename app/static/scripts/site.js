(function ($) {
    "use strict"; // Start of use strict


    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 56
    });
    // Collapse Navbar
    var navbarCollapse = function () {
        console.log("miau");
        if ($("#mainNav").offset().top > 100) {
            console.log("add");
            $("#mainNav").addClass("navbar-shrink");
        } else {
            console.log("else");
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery);