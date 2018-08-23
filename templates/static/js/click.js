$(document).on('click','.spider_url', function () {
   // $(".spider_url").first().addClass("click-bgcolor");
   $(".spider_url").click(function(){  //点击事件添加click-bgcolor
      $(this).addClass("click-bgcolor").siblings().removeClass("click-bgcolor");
   })
});