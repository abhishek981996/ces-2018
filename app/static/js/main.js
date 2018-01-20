$(document).ready(function() {

  'use strict';

/***************
SLIDES
***************/

  $('#slides').superslides({
    animation: "fade",
    navigation: false,
    pagination: false
  });

/***************
SCROOL
***************/
  smoothScroll.init({
    speed: 1000,
    easing: 'easeInOutCubic',
    updateURL: false,
    offset: 100,
    callbackBefore: function(toggle, anchor) {},
    callbackAfter: function(toggle, anchor) {}
  });

/***************
WORKS RESPONSIVE
***************/

  $(window).resize(responsive);
  $(window).trigger('resize');

/***************
ANIMATIONS
***************/

  var wow = new WOW(
    {
        boxClass:     'wow',      // animated element css class (default is wow)
        offset:       0,          // distance to the element when triggering the animation (default is 0)
        animateClass: 'animated', // animation css class (default is animated)
        mobile:       false        // trigger animations on mobile devices (true is default)
      }
    );
  wow.init();

/***************
BLOG
***************/

  var list = $(".blog-items li");
    var numToShow = 1;
    var button = $("#next-blog");
    var numInList = list.length;
    list.hide();
    if (numInList > numToShow) {
      button.show();
    }
    list.slice(0, numToShow).show();

    button.on('click', function(){
        var showing = list.filter(':visible').length;
        list.slice(showing - 1, showing + numToShow).fadeIn();
        var nowShowing = list.filter(':visible').length;
        if (nowShowing >= numInList) {
          button.hide();
        }
    });

/***************
CLIENTS
***************/

  var owlClients = $("#owl-clients");
 
    owlClients.owlCarousel({
       
      itemsCustom : [
        [0, 2],
        [414, 2],
        [500, 3],
        [768, 3],
        [1000, 5],
        [1600, 5]
      ],
      navigation : false,
      pagination:false 
  });

/***************
TEAM
***************/

  var owlTeam = $("#owl-team");

  owlTeam.owlCarousel({
    items : 8, //10 items above 1000px browser width
    itemsDesktop : [2650,4], //5 items between 1000px and 901px
    itemsDesktopSmall : [992,3], // betweem 900px and 601px
    itemsTablet: [600,2], //2 items between 600 and 0
    itemsMobile : [414,1], // itemsMobile disabled - inherit from itemsTablet option
    pagination:false
  });

  // Custom Navigation Events
  $(".next").on('click', function(){
   owlTeam.trigger('owl.next');
  });

  $(".prev").on('click', function(){
   owlTeam.trigger('owl.prev');
  });

/***************
WORKS ITEM
***************/

  var owlWorkItem =$(".owl-works-item");
    owlWorkItem.owlCarousel({ 
      navigation : false, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      pagination:false,
      singleItem:true 
      // "singleItem:true" is a shortcut for:
      // items : 1, 
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false 
    });

    // Custom Navigation Events
  $(".next-work").on('click', function(){
   owlWorkItem.trigger('owl.next');
  });
  $(".prev-work").on('click', function(){
   owlWorkItem.trigger('owl.prev');
  });

/***************
WORKS PAGE
***************/

  var owlWorkPageItem =$(".owl-works-page-item");
  owlWorkPageItem.owlCarousel({

    navigation : false, // Show next and prev buttons
    slideSpeed : 300,
    pagination:false,
    paginationSpeed : 400,
    singleItem:true

    // "singleItem:true" is a shortcut for:
    // items : 1, 
    // itemsDesktop : false,
    // itemsDesktopSmall : false,
    // itemsTablet: false,
    // itemsMobile : false
 
  });

    // Custom Navigation Events
  $(".next-work-page").on('click', function(){
    owlWorkPageItem.trigger('owl.next');
  });
  
  $(".prev-work-page").on('click', function(){
    owlWorkPageItem.trigger('owl.prev');
  });

/***************
GOOGLE MAP
***************/

  var styles = [
    {
        "featureType": "administrative",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#444444"
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "all",
        "stylers": [
            {
                "color": "#f2f2f2"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "all",
        "stylers": [
            {
                "saturation": -100
            },
            {
                "lightness": 45
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "simplified"
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "all",
        "stylers": [
            {
                "color": "#e8e8e8"
            },
            {
                "visibility": "on"
            }
        ]
    }
  ]; 

  if ($("#map").length > 0){
   
  var map = new GMaps({
    el: '#map',
    lat: 21.161521,
    lng: 72.7844565,
    zoom: 15,
    draggable: false,
    scrollwheel: false,
    disableDoubleClickZoom: true,
    zoomControl: false,
    backgroundColor: '#FFFFFF',
    styles: styles
  });


  map.drawOverlay({
    lat: 21.161851,
    lng: 72.7844565,
    content: '<div class="overlay"></div><div class="overlay_arrow above"></div>'
  });

 }
/***************
LOADING
***************/

  $(window).load(function() {
  
    // extra load time for your eyes only!
    setTimeout(function() {
  
      // remove "pulsate" animation from logo
      $('#logo').removeClass('active');
  
      // kick in the transistions
      $('#loadWrapper, #overlay').addClass('loaded');
  
    }, 1000);
  
    // hide load elements from DOM
    setTimeout("$('#loadWrapper').addClass('hide')", 4000);
    setTimeout("$('#logo').addClass('hide')", 4500);
    setTimeout("$('#overlay').addClass('hide')", 5000);
  
    // remove load elements from DOM
    setTimeout("$('#load').remove();", 4000);
  
  });

});



/***************
WORKS RESPONSIVE FUNCTIONS
***************/

function responsive(){
  'use strict';
  // get resolution
  var resolution = document.documentElement.clientWidth;

  // because mobile layout
  if (resolution < 415) {
  
    if( $('.select-menu').length === 0 ) {
      
      // create select menu
      var select = $('<select id="works-select"></select>');

      // add classes to select menu
      select.addClass('select-menu input-block-level');

      // each link to option tag
      $('.works-tabs li a').each(function(){
        // create element option
        var option = $('<option></option>');

        // add href value to jump
        option.val(this.href);

        // add text
        option.text($(this).text());

        // append to select menu
        select.append(option);
      });

      // add change event to select
      $(document).on("change","#works-select",function(){
         var tab = ($(this)[0].selectedIndex)+1;
        $('.works-tabs a[href="#tab' + tab + '"]').tab('show');
      });


      // add select element to dom, hide the .nav-tabs
      $('.works-tabs').before(select).hide();

    }

  }

  // max width 979px
  if (resolution > 415) {
    $('.select-menu').remove();
    $('.works-tabs').show();
  }

}