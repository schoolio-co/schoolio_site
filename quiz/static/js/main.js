"use strict";

$(document).ready(function(){
	// * Preloader *
    $('.loader').fadeOut();    
    $('#preloader').delay(200).fadeOut('slow');
	//* mobile navigation *
	var mobileNav = $(".mobile-nav");
	mobileNav.on("click",function(){
	$('.nav-menu').toggleClass('mobile-menu-open');
	mobileNav.toggleClass('bg-nav');
});

// * Home-Carousel *
    var swiper = new Swiper('.swiper-container', {
      speed: 600,
      parallax: true,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      breakpoints: {
        480: {
         	pagination: {
        	el: false,
      		},
        }
      }
    });

// * owlCarousel *
$(".clients-slide").owlCarousel({
	center: true,
	loop: true,
	autoplay: true,
	autoWidth:true,
	responsiveClass:true,
	margin:30,
});

// * Progressbar *
var skillsDiv = $('#skills');
var aboutId = $('#about');
var skillBar = $('.skillbar');

 $.fn.hasScrollBar = function() {
    return this.get(0).scrollHeight > this.height();
    };
    
if(aboutId.hasScrollBar() == false){
	skillBar.each(function(){
      $(this).find('.skillbar-bar').animate({
        width:$(this).attr('data-percent')
      },1000);
    });
}

aboutId.bind('scroll', function(){
	var winT = $(window).scrollTop(),
  	winH = $(window).height(),
  	skillsT = skillsDiv.offset().top;
  if(winT + winH  > skillsT){
  	skillBar.each(function(){
      $(this).find('.skillbar-bar').animate({
        width:$(this).attr('data-percent')
      },1000);
    });
  }
});

//* PORTFOLIO *
/* initialize shuffle plugin */
	 var $grid = $('#grid');
	 var filter = $('#filter a');

$grid.imagesLoaded( function() {
	 $grid.shuffle({
		// itemSelector: '.item' // the selector for the items in the grid
		 itemSelector: '.item'
	 });
});               

	/* reshuffle when user clicks a filter item */
	filter.on('click',function (e) {
		e.preventDefault();
		// set active class
		filter.removeClass('active-filter');
		$(this).addClass('active-filter');
		// get group name from clicked item
		var groupName = $(this).attr('data-group');
		// reshuffle grid
		$grid.shuffle('shuffle', groupName );
	});


// * transition page *
var section = window.location.hash,
	secAbout = $('a[href = "#about"]'),
	secContact =$('a[href = "#contact"]'),
	profileImg = $('.panel-2'),
	panelCart = $('.panel-cart'),
	secActive = $(".menu-text a[href='"+section+"']"),
	menuText = $('.menu-text a');

$('a').on('click', function(){
	var element = $(this);
    if(element !== secAbout){
        profileImg.removeClass('profile-img-left');
    }
    if(element != secContact){
    	panelCart.removeClass('cart-open');
    }
});

secAbout.on('click', function() {
	profileImg.addClass('profile-img-left');
      });

secContact.on('click', function() {
	panelCart.addClass('cart-open');
      });

//event page reload 
if(section == "#about"){
	profileImg.addClass('profile-img-left');
}
if(section == "#contact"){
	panelCart.addClass('cart-open');
}
if(secActive == secActive){
	menuText.removeClass('active-filter');
	secActive.addClass('active-filter');
}
if("" == section){
	$(".menu-text a[href='#home']").addClass('active-filter');
}

//(events)browser buttons back and forth
addEventListener("popstate",function(e){
	var section = window.location.hash;
	if(section == "#about"){
	profileImg.addClass("profile-img-left");
	}else{
	profileImg.removeClass("profile-img-left");
	}
	if(section == "#contact"){
		panelCart.addClass('cart-open');
	}else{
		panelCart.removeClass('cart-open');
	}
	if(section == ""){
	menuText.removeClass('active-filter');	
	$(".menu-text a[href='#home']").addClass('active-filter');
	}

	if(section == "#about"){
		menuText.removeClass('active-filter');	
    	$(".menu-text a[href='#about']").addClass('active-filter');
	}
	if(section == "#portfolio"){
		menuText.removeClass('active-filter');	
    	$(".menu-text a[href='#portfolio']").addClass('active-filter');
	}
	if(section == "#resume"){
		menuText.removeClass('active-filter');	
    	$(".menu-text a[href='#resume']").addClass('active-filter');
	}
	if(section == "#contact"){
		menuText.removeClass('active-filter');	
    	$(".menu-text a[href='#contact']").addClass('active-filter');
	}
	if(section == "#home"){
		menuText.removeClass('active-filter');	
    	$(".menu-text a[href='#home']").addClass('active-filter');
	}
});

// * menu-nav *
// button 
$("a.button").on("click", function(){
	   var attrButton = $(this).attr('href');
	   menuText.removeClass('active-filter');
	   $(".menu-text a[href='"+attrButton+"']").addClass('active-filter');
});

menuText.on('click',function () {
				menuText.removeClass('active-filter');
	   $(this).addClass('active-filter');
			});

//* Magnific-popup *
$('div.item>a').magnificPopup({
		type: 'image',
		closeBtnInside: false,
    closeOnContentClick: true,

    gallery: {
      enabled: true,
      tCounter: '<span class="mfp-counter">%curr% / %total%</span>' ,
    }
  
	});

});