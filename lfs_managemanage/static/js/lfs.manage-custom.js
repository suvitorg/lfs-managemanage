$.get('/manage/manage/', function(config){
  $(document).ready(function(){
    if (config['mainmenu'])
      $('ul.sf-menu').replace(config['mainmenu']);
  });
});
