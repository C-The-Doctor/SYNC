$( document ).ready(function() {
  var username = 'andytran';

  $('input').keyup(function() {
    username = $(this).val();

    $('label').text(username);

    getData(username);
  });

  getData = function(username) {
    $.getJSON('http://cpv2api.com/profile/' + username, function(resp) {
      if (resp.success) {
        console.log('Successful');

        $('.card-header__avatar').css('background-image', 'url(' + resp.data.avatar + ')');
        $('.card-header__follow').attr('href', 'https://codepen.io/' + resp.data.username);


        if (resp.data.pro) {
          $('.card-content__username').text(resp.data.nicename);
          $('.card-content__username').append('<span class="badge">PRO</span>');
        } else {
          $('.card-content__username').text(resp.data.nicename);
        }

        if (resp.data.bio) {
          $('.card-content__bio').text(resp.data.bio);
        } else {
          $('.card-content__bio').text('Demo or it didn\'t happen.');
        }

        $('.card-footer__pens span').text(Math.floor((Math.random() * 100) + 1));

        $('.card-footer__followers span').text(resp.data.followers);
        $('.card-footer__following span').text(resp.data.following);
      } else {
        $('.card-header__avatar').css('background-image', 'url(http://placehold.it/500/000/fff)');
        $('.card-content__username').text('CodePen');
        $('.card-content__username').append('<span class="badge">PRO</span>');
        $('.card-content__bio').text('Demo or it didn\'t happen.');
        $('.card-footer__followers span').text('1337');
        $('.card-footer__following span').text('1337');
      }

      getHTML();
    });
  }

  getHTML = function() {
    var cardHTML = $('.container').html();

    $('.code').text(cardHTML);
  }

  getData(username);
});