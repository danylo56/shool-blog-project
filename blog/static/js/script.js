$(document).ready(function(){
  let delayTimer;
  $('#id_search_term').keyup(function () {
    clearTimeout(delayTimer);
    $('#search_results').text("Пошук...");
    delayTimer = setTimeout(function(){
      let text = document.getElementById('id_search_term').value;
      console.log(text);
      $.ajax({
        url: '/blog/search_blog',
        data: {
          'search_term': text,
        },
        dataType: 'json',
        success: function(data){
          let result = '';
          if(data['error']){
            result += '<div class="alert Alert-info">Помилка пошуку</div>'
          }else{
              data['results'].forEach(blog => {
                result += '<div class="row">\
                        <div class="col-md-4 d-flex justify-content-md-start justify-content-center">\
                              <img src="'+ blog.image_url + '" alt="Фото '+ blog.title + '" width="200px">\
                          </div>\
                          <div class="col-md-8">\
                              <h2><a class="text-decoration-none text-dark" href="/blog/' + blog.id + '">' + blog.title + '</a></h2>\
                              <p>' + blog.text + '</p>\
                              <p>' + blog.pub_date + '</p>\
                          </div>\
                      </div>\
                      <hr>'
              });
              $('#search_results').text('');
              $('#search_results').append(result);
          }
        }
      });
    }, 1000);
  });
});
