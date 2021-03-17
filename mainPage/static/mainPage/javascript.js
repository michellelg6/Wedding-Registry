$( document ).ready(function() {
var $a = $("a");

$a.click(function() {

   $a.removeClass("active");
   $(this).addClass("active");

$("h1").html($(".active").text());
});
});

