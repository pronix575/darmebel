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

	function sleep(milliseconds) {
	  var start = new Date().getTime();
	  for (var i = 0; i < 1e7; i++) {
	    if ((new Date().getTime() - start) > milliseconds){
	      break;
	    }
	  }
	}

	$(".nativeMenu").toggle()	

	var trigger = true
	$( ".menuBtn1" ).click(function(){ 
		if (trigger) {
			if (!tr) {
				$(".nativeSearch").toggle()
				$("#searchBtn").each(function(i,elem) {
					$(elem).toggleClass('fa fa-close fa-lg').toggleClass('fa fa-search fa-lg');
				})	
				tr = true
			}

		  	$(".nativeMenu").show()
			$('#navicon').toggleClass('fa fa-navicon fa-lg').toggleClass('fa fa-close fa-lg');
		  	trigger = false
		} else {
			$(".nativeMenu").toggle()
		  	$('#navicon').toggleClass('fa fa-close fa-lg').toggleClass('fa fa-navicon fa-lg');
			trigger = true
		}
	});

	$(".nativeSearch").toggle()
	
	var tr = true
	$(".search").click(function(){
		if (tr) {

			if (!trigger) {
				$(".nativeMenu").toggle()
				$('#navicon').toggleClass('fa fa-close fa-lg').toggleClass('fa fa-navicon fa-lg');
				trigger = true
			}
			$("#searchBtn").each(function(i,elem) {
		  		$(elem).toggleClass('fa fa-search fa-lg').toggleClass('fa fa-close fa-lg');
		  	})
		  	 // $(".nativeSearch").css("backdrop-filter", "blur(1px)")
		  	$(".nativeSearch").css("padding-top", 40)
		  	$(".nativeSearch").css("opacity", 0.2)
		  	
		  	$(".nativeSearch").show()
		  	$(".nativeSearch").animate({"padding-top": "30px", "opacity": "1"}, 0.1);

		  	tr = false
		
		} else {
			$(".nativeSearch").toggle()
			$("#searchBtn").each(function(i,elem) {
				$(elem).toggleClass('fa fa-close fa-lg').toggleClass('fa fa-search fa-lg');
			})
			tr = true
		}
	});
		if ($(".noname").html() == "hello") {			
			$(".search").css("display", "none")
		}

	$(window).resize(function(){
		if (screen.width > 650 && !trigger) {
			$(".nativeMenu").toggle()
			
			if (tr) {
				$('#navicon').toggleClass('fa fa-navicon fa-lg').toggleClass('fa fa-close fa-lg');
			}	
			trigger = true
		}

		if (screen.width < 650 && !tr) {

		}

		resizeOfFont()

	});

});