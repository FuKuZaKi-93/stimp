$(".likeform").click(function() {
    $('.likeform').submit(function() {
        $.ajax({
            'url': $(this).attr('action'),
            'type':'POST',
            }).done(function(response){
                var thisform = $(this).attr('id')
                $('input[name=thisform]').toggleClass('btn-default btn-success');
                alert(response.message);
                //$(this).data('condition',true);
        });
    return false;
    });
});

/*
$(".favoButton").click(function() {
    if($(this).data('condition') == false){
        $('.favoButton').submit(function() {
            $.ajax({
                'url': $(this).attr('action'),
                'type':'POST',
                'data': {'favonum':$(this).data('favonum')},
                'dataType':'jsonp',
                })
                .done(function(response){
                    $(this).css('backgroundColor', '#FF0');
                    $(this).data('condition',true);
            });
        return false;
        });
    }else{
    if($(this).data('condition') == true){
        $('.favoButton').submit(function() {
            $.ajax({
                'url': $(this).attr('action'),
                'type':'POST',
                'data': {'favonum':$(this).data('favonum')},
                'dataType':'json',
                'success':function(response){
                    $(this).css('backgroundColor', '');
                    $(this).data('condition',false);
                    alert("ok!");
                },
            });
        return false;
        });
    }};
});*/
