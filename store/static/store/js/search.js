$(document).ready(function(){
	var $pront = $(".price")
	
	var 	price       = $pront.html(),
            price_sep   = price.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1 ");	   

            $pr.empty()

            $pr.html(price_sep + " ₽")

});