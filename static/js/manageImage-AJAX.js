$(document).ready(function() {
    $('.likeButton').click(function() {
        console.log("LIKE CLICKED");
        var catecategoryIdVar;
        pictureIdVar = $(this).attr('data-pictureID');

        $.get('/like_picture/',
            {'picture_id': pictureIdVar},
            function(data) {
                console.log(data);
                var splitData = data.split(':');
                $('#like-count' + pictureIdVar).html(splitData[1]);
                $('#dislike-count' + pictureIdVar).html(splitData[0]);
            })
    });

    $('.shareButton').click(function() {
        console.log("DISLIKE CLICKED");
        var catecategoryIdVar;
        pictureIdVar = $(this).attr('data-pictureID');

        $.get('/dislike_picture/',
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
});