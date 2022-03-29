$(document).ready(function() {
    $('.likeButton').click(function() {
        console.log("LIKE CLICKED");
        pictureIdVar = $(this).attr('data-pictureID');

        $.get('/images/like_picture/',
            {'picture_id': pictureIdVar},
            function(data) {
                console.log(data);
                var splitData = data.split(':');
                $('#like-count' + pictureIdVar).html(splitData[1]);
                $('#dislike-count' + pictureIdVar).html(splitData[0]);
            })
    });

    $('.dislikeButton').click(function() {
        console.log("DISLIKE CLICKED");
        pictureIdVar = $(this).attr('data-pictureID');

        $.get('/images/dislike_picture/',
            {'picture_id': pictureIdVar},
            function(data) {
                console.log(data);
                var splitData = data.split(':');
                $('#like-count' + pictureIdVar).html(splitData[1]);
                $('#dislike-count' + pictureIdVar).html(splitData[0]);
            })
    });

    $('.shareButton').click(function(){
        pageLink = $(location).attr("href");
        navigator.clipboard.writeText(pageLink).then(function () {
            alert('Link copied to clipboard')
        }, function () {
            alert("Your browser doesn't support the clipboard API")
        });
    })

    $('.followButton').click(function() {
        console.log("FOLLOW CLICKED");
        userVar = $(this).attr('data-user');

        $.get('/login/follow/',
            {'user': userVar},
            function(data) {
                console.log(data);
                $('#buttontext').html(data);
            })
    });

});