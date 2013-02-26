$.get('/manage/manage/', function(config){
  console.log(config);
  $(document).ready(function(){
    if (config['LFS_MANAGE_MAINMENU']){
      $('ul.sf-menu').html(config['LFS_MANAGE_MM_RENDERED']);
      }
  });
});
