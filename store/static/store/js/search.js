$(document).ready(function(){

	$(".price").each(function(i,elem) {
		var price = $(elem).html()	   

	    $(elem).empty()

	    $(elem).html(price.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1 "))
	});

	function resizeOfFont() {
		$(".nameOfFurniturePreview").each(function(i,elem) {
			var nameOfFurniturePreview = $(elem).html()
			var wid = screen.width, tSize = 0

	    	tSize = 30

	    	if (wid < 720) {
	    		tSize = 20
	    	}
    		
    		if (wid < 500) {
    			tSize = 13
    		}
	    	if (wid < 500) {
	    		tSize = 11
	    	}
			
			if (nameOfFurniturePreview.length > tSize) {
				$(elem).empty()
				$(elem).html(nameOfFurniturePreview.substr(0, tSize) + "...")
			}
		});
	}

	resizeOfFont()

	$(".nativeMenu").toggle()

	trigger = true
	$( ".menuBtn1" ).click(function(){ 
		if (trigger) {
		  	$(".nativeMenu").show()
		  	$('#navicon').toggleClass('fa fa-navicon fa-lg').toggleClass('fa fa-close fa-lg');
		  	trigger = false
		} else {
			$(".nativeMenu").toggle()
			$('#navicon').toggleClass('fa fa-close fa-lg').toggleClass('fa fa-navicon fa-lg');
			trigger = true
		}
	 });

	$(window).resize(function(){
		if (screen.width > 650 && trigger != true) {
			$(".nativeMenu").toggle()
			$('#navicon').toggleClass('fa fa-close fa-lg').toggleClass('fa fa-navicon fa-lg');
			trigger = true
		}
		resizeOfFont()
	});

});