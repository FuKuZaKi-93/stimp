$('#getform').submit(function() {
    $('#result').html('');
    $.ajax({
        'url':'{% url "api_v1_posts" %}',
        'type':'GET',
        'data':{
            'query':$('#query').val(),
        },
        'dataType':'json',
        'success':function(response){
            $.each(response.result_list, function(index, title) {
                $('#result').append('<p>'+ title +'</p>')
            });              
        },
    });
    return false;
});
$('#postform').submit(function() {
    $.ajax({
        'url':'{% url "api_v1_posts" %}',
        'type':'POST',
        'data':{
            'title':$('#title').val(),
        },
        'dataType':'json',
        'success':function(r){
            message = 'pk→' + r.pk +  '\ntitle→' + r.title + '\n日付→'+ r.created_at;
            alert(message);           
        },
    });
    return false;
});
