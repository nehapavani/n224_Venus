$('.sm-days').click(function() {

    if ($(this).find('.day-weather-icon > i').hasClass('wi-day-showers')) {
        $('body').css({
            'background': 'url(https://ununsplash.imgix.net/18/trickle.JPG?fit=crop&fm=jpg&h=700&q=75&w=1050) center center / cover fixed'
        });
    }

    if ($(this).find('.day-weather-icon > i').hasClass('wi-cloudy')) {
        $('body').css({
            'background': 'url(https://ununsplash.imgix.net/36/q3Y09XWNRRC5Et7bEQnE_beach-alex-talmon.jpg?fit=crop&fm=jpg&h=700&q=75&w=1050) center center / cover fixed'
        });
    }

    if ($(this).find('.day-weather-icon > i').hasClass('wi-showers')) {
        $('body').css({
            'background': 'url(https://unsplash.imgix.net/photo-1432836431433-925d3cc0a5cd?fit=crop&fm=jpg&h=700&q=75&w=1050) center center / cover fixed'
        });
    }

    if ($(this).find('.day-weather-icon > i').hasClass('wi-day-lightning')) {
        $('body').css({
            'background': 'url(https://unsplash.imgix.net/16/unsplash_5252b10dacd20_1.JPG?fit=crop&fm=jpg&h=700&q=75&w=1050) center center / cover fixed'
        });
    }

    if ($(this).find('.day-weather-icon > i').hasClass('wi-day-sunny')) {
        $('body').css({
            'background': 'url(https://unsplash.imgix.net/photo-1422405153578-4bd676b19036?fit=crop&fm=jpg&h=700&q=75&w=1050) center center / cover fixed'
        });
    }

// Weather Info Replacement
    var icon = $(this).find('i').attr("class");
    var temp = $(this).find('.day-weather-info').html();
    var day = $(this).find('.day').html();

    $('.current-city-weather>i').removeClass().addClass(icon);
    $('.current-city-temp').html(temp);
    $('.current-city-day').html(day);

    $('.current-city-weather').addClass('fadeInUp');
    setTimeout(function() {
        $('.current-city-weather').removeClass('fadeInUp');
    }, 1000);
});