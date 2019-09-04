/* ========================================================================

Zien: Main.js ( Main Theme JS file )

Theme Name: Zien - Creative Portfolio Landing Page
Version: 1.0
Author: Raven Themez
Author URI: http://themeforest.net/user/raventhemez
If you having trouble in editing js. please send a mail to raventhemez@gmail.com

=========================================================================
 */


"use strict";


/*======== Doucument Ready Function =========*/
jQuery(document).ready(function () {

    //CACHE JQUERY OBJECTS
    var $window = $(window);

    $window.on( 'load', function () {
        /*======== Preloader =========*/
        $(".loading-text").fadeOut();
        $(".loading").delay(350).fadeOut("slow");
        /* END of Preloader */

        /*========= Masonry Grid Script ==========*/
        $(".grid-masonry").masonry({
            // options...
            itemSelector: ".grid-item",
            columnWidth: ".grid-item",

        });
        /*========== End Masonry Grid ==========*/

        /*========== Init Wow ==========*/
        new WOW().init();
        /*========== End Init Wow ==========*/

    });

    /*======== Menu Init =========*/

    if ($window.width() > 767) {
        $(".dropdown").on('mouseenter', function(){
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).slideDown(200);
            $(this).toggleClass('open');
        });
        $(".dropdown").on('mouseleave', function(){
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).slideUp(200);
            $(this).toggleClass('open');
        });
    }

    /*======= jQuery navbar on scroll =========*/

    $window.on('scroll' , function () {

        if ($(".navbar-default").add(".navbar-inverse").offset().top > 50) {
            $(".reveal-menu-home").addClass("sticky-nav");
            $(".reveal-menu-blog").addClass("sticky-nav-white");
        } else {
            $(".reveal-menu-home").removeClass("sticky-nav");
            $(".reveal-menu-blog").removeClass("sticky-nav-white");
        }
    });

    /*======= End jQuery navbar on scroll =========*/



    /*======== End Menu Init =========*/

    /*======= Banner Resize with window size =========*/

    $window.on( 'resize', function () {
        var bodyheight = $(this).height();
        $("#mt_banner").height(bodyheight);
    }).resize();

    /*======= End Banner Resize with window size =========*/

    /*======= Main Slider Init =========*/

    var interleaveOffset = 0.5;
    var swiperOptions = {
        loop: true,
        speed: 1000,
        grabCursor: true,
        watchSlidesProgress: true,
        mousewheelControl: true,
        keyboardControl: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        on: {
            progress: function() {
                var swiper = this;
                for (var i = 0; i < swiper.slides.length; i++) {
                    var slideProgress = swiper.slides[i].progress;
                    var innerOffset = swiper.width * interleaveOffset;
                    var innerTranslate = slideProgress * innerOffset;
                    swiper.slides[i].querySelector(".slide-inner").style.transform =
                        "translate3d(" + innerTranslate + "px, 0, 0)";
                }
            },
            touchStart: function() {
                var swiper = this;
                for (var i = 0; i < swiper.slides.length; i++) {
                    swiper.slides[i].style.transition = "";
                }
            },
            setTransition: function(speed) {
                var swiper = this;
                for (var i = 0; i < swiper.slides.length; i++) {
                    swiper.slides[i].style.transition = speed + "ms";
                    swiper.slides[i].querySelector(".slide-inner").style.transition =
                        speed + "ms";
                }
            }
        }
    };
    var swiper = new Swiper(".swiper-container", swiperOptions);

    /*======= End Main Slider Init =========*/


    /*======= Portfolio =========*/

    var mt_personal = window.mt_personal || {},
        $win = $(window);

        mt_personal.Isotope = function () {

        // 4 column layout
        var isotopeContainer = $(".isotopeContainer");
        if (!isotopeContainer.length || !jQuery().isotope) return;
        $win.load(function () {
            isotopeContainer.isotope({
                itemSelector: ".isotopeSelector"
            });
            $(".mt_filter").on("click", "a", function (e) {
                e.preventDefault();
                $(".mt_filter ul li").find(".active").removeClass("active");
                $(this).addClass("active");
                var filterValue = $(this).attr("data-filter");
                isotopeContainer.isotope({ filter: filterValue });
                e.preventDefault();
            });
        });

    };

    mt_personal.Isotope();

    /*======= End Portfolio =======*/

    /*======= Progress Bar =========*/

    var progress_way = $('.mt_skill-progress');
    if (progress_way.length > 0) {
        progress_way.waypoint(function() {
            jQuery('.mt_skill-bar').each(function() {
                jQuery(this).find('.progress-content').animate({
                    width: jQuery(this).attr('data-percentage')
                }, 2000);
                jQuery(this).find('.progress-mark').animate({
                    left: jQuery(this).attr('data-percentage')
                }, {
                    duration: 2150,
                    step: function(now, fx) {
                        var data = Math.round(now);
                        jQuery(this).find('.percent').html(data + '%');
                    }
                });
            });
        }, {
            offset: '90%'
        });
    }

    /*======= End Progress Bar =======*/


    /*======== One Page Scrolling ======= */

    $(".main-nav").onePageNav({
        currentClass: "active",
        changeHash: true,
        scrollSpeed: 1000,
        scrollThreshold: 0.5,
        filter: "",
        easing: "swing",
        begin: function () {
            //I get fired when the animation is starting
        },
        end: function () {
            //I get fired when the animation is ending
        },
        scrollChange: function ($currentListItem) {
            //I get fired when you enter a section and I pass the list item of the section
        }
    });

    $( 'a[href*=#]:not([href=#])' ).on('click', function(e){
        e.preventDefault();
        if( location.pathname.replace( /^\// , '' ) == this.pathname.replace( /^\// , '' ) && location.hostname == this.hostname )
        {
            var target = $( this.hash );
            if( target.length )
            {
                $( 'html,body' ).stop().animate(
                {
                    scrollTop:target.offset().top - 80
                } , 1000 );
                return false;
            }
        }
    });

    /*======== End One Page Scrolling ========*/

    /*======== Contact Form ========*/

    $('#submit-btn').on('click',function (event){
        event.preventDefault();
        $.ajax({
            dataType: 'JSON',
            url: 'sendmail.php',
            type: 'POST',
            data: $('#contact_form').serialize(),
            beforeSend: function (xhr) {
                $('.mt_load').show();
            },
            success: function (response) {
                if (response) {
                    console.log(response);
                    if (response['signal'] == 'ok') {
                        toastr.success(response['msg']);
                        $('#msg').hide();
                        $('input, textarea').val(function () {
                            return this.defaultValue;
                        });
                    }
                    else {
                        $('#msg').show();
                        $('#msg').html('<div class="mt_error">'+ response['msg'] +'</div>');
                    }
                }
            },
            error: function () {
                $('#msg').show();
                $('#msg').html('<div class="mt_error">Errors occur. Please try again later.</div>');
            },
            complete: function () {
                $('.mt_load').hide();
            }
        });
    });
    /*======== End Contact Form ========*/


    /*======== Fancy Box Init ========*/

    var FancYB = $('.fancybox');
    FancYB.fancybox({
        openEffect: 'fade',
        closeEffect: 'fade',
        padding : 0,
        closeBtn: true,
        helpers: {
            title: {
                type: 'inside'
            },
            overlay: {
              locked: false
            },
            buttons: {}
        }
    });
    FancYB.attr('rel','gallery');

    /*======== End Fancy Box ========*/

    /*======== Brand Slider =========*/

    $("#mt_client .owl-carousel").owlCarousel({
        loop: false,
        margin: 24,
        autoplay: false,
        autoplayHoverPause: true,
        autoplaySpeed: 1000,
        dot: true,
        smartSpeed:850,
        responsive: {
            0: {
                items: 1,
                dots: true
            },
            600: {
                items: 3,
                dots: true
            },
            1000: {
                items: 5,
                dots: true
            },
            1201: {
                items: 5,
                dots: true
            }
        }
    });
    /*======== End Brand Slider =========*/
    /*======== Team Section =========*/
    $("#mt_team .owl-carousel").owlCarousel({
        loop: false,
        autoplay: false,
        autoplayHoverPause: false,
        autoplaySpeed: 1000,
        smartSpeed:850,
        responsive: {
            0: {
                items: 1,
                dots: true
            },
            450: {
                items: 2,
                dots: true
            },
            500: {
                items: 2,
                dots: true
            },
            600: {
                items: 2,
                dots: true
            },
            1000: {
                items: 4,
                dots: true
            },
            1201: {
                items: 4,
                dots: true
            }
        }
    });

    /*======== End Team Section =========*/
    /*======== Testimonial Section =========*/

    $("#mt_testimonial .owl-carousel").owlCarousel({
        loop: false,
        margin: 24,
        autoplay: false,
        autoplayHoverPause: true,
        autoplaySpeed: 1000,
        dot: true,
        smartSpeed:850,
        responsive: {
            0: {
                items: 1,
                dots: true
            },
            600: {
                items: 1,
                dots: true
            },
            1000: {
                items: 2,
                dots: true
            },
            1201: {
                items: 2,
                dots: true
            }
        }
    });

    /*======== End Testimonial Section =========*/
    /*======== Portfolio Detail 1 Section =========*/

    $(".project_gallery .owl-carousel").owlCarousel({
        center: true,
        loop: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsiveBaseElement: window,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2,
                nav: true
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 2,
                nav: true
            },
            1201: {
                items: 2,
                nav: true
            }
        }
    });

    /*======== End Portfolio Detail 1 Section =========*/

    /*======== Portfolio Gallery 2 =========*/

    $(".portfolio_gallery .owl-carousel").owlCarousel({
        center: true,
        loop: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsiveBaseElement: window,
        responsiveClass: true,
        navText: ["<img src='images/arrow-left.png'>","<img src='images/arrow-right.png'>"],
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            600: {
                items: 1,
                nav: true
            },
            1000: {
                items: 1,
                nav: true
            },
            1201: {
                items: 1,
                nav: true
            }
        }
    });

    /*======== End Portfolio Gallery2 =========*/

});
/*======== End Doucument Ready Function =========*/