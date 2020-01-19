$(document).ready(function(){

	$(".price").each(function(i,elem) {
		var price = $(elem).html()	   

	    $(elem).empty()

	    $(elem).html(price.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1 "))
	});
});