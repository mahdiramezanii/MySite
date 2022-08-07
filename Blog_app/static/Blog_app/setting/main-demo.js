$(function() {

    $('.style-options').addClass('active');
    setTimeout(function(){
        $('.style-options').removeClass('active');
    }, 5000);

    $('.style-options .toggle-btn').on('click', function() {
        $('.style-options').toggleClass('active');
    });

    $('.theme-style li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.theme-st').attr('href', style_link);

        e.preventDefault();
    });

	$('.style-nav li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.pos-nav').attr('href', style_link);

        e.preventDefault();
    });

	$('.box-body li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.box-bd').attr('href', style_link);

        e.preventDefault();
    });

	$('.box-style li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.box-st').attr('href', style_link);

        e.preventDefault();
    });

	$('.box-title li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.box-tl').attr('href', style_link);

        e.preventDefault();
    });

	$('.box-title-st li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.box-tl-st').attr('href', style_link);

        e.preventDefault();
    });

	$('.style-color li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.style-cl').attr('href', style_link);

        e.preventDefault();
    });

});