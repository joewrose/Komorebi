$(document).ready(function() {

    $('.likeButton').click(function() {
        console.log("LIKE CLICKED");
        var catecategoryIdVar;
        pictureIdVar = $(this).attr('data-pictureID');

        $.get('/like_picture/',
            {'picture_id': pictureIdVar},
            function(data) {
                $('#like-count' + pictureIdVar).html(data);
            })
    });
});