gisportal.slideRight = function(){
$('#scroller_container').animate({left: 0},{duration: 500, queue: false}); $('#right_panel').animate({left: 1920},{duration: 500, queue: false});

};

gisportal.slideLeft = function(){
   $('#scroller_container').animate({left: -1920},{duration: 500, queue: false}); $('#right_panel').animate({left: 0},{duration: 500, queue: false});

};