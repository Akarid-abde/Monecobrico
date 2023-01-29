$(document).ready(function() {
    $("#news-slider").owlCarousel({
        items : 3,
        itemsDesktop:[1199,3],
        itemsDesktopSmall:[980,2],
        itemsMobile : [600,1],
        navigation:true,
        navigationText:["",""],
        pagination:true,
        loop: true,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsive: {
             0:{
               items:1,
               nav: false
             },
             600:{
               items:2,
               nav: false
             },
             1000:{
               items:3,
               nav: false
             }
           }
    });
});

$('#moreless-button1').click(function() {
  $('.moretext1').slideToggle();
});
$('#moreless-button2').click(function() {
  $('.moretext2').slideToggle();

});
$('#moreless-button3').click(function() {
  $('.moretext3').slideToggle();

});
$('#moreless-button4').click(function() {
  $('.moretext4').slideToggle();

});
$('#moreless-button5').click(function() {
  $('.moretext5').slideToggle();

});
$('#moreless-button6').click(function() {
  $('.moretext6').slideToggle();

});