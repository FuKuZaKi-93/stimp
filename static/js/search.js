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
