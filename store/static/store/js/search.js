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

	    	tSize = 25
    		
    		if (wid < 500) {
    			tSize = 18
    		}
	    	if (wid < 350) {
	    		tSize = 14
	    	}
			
			if (nameOfFurniturePreview.length > tSize) {
				$(elem).empty()
				$(elem).html(nameOfFurniturePreview.substr(0, tSize) + "...")
			}
		});
	}

	function resizeOfFontR() {
		if (screen.width / screen.height > 1.9) {
			mainHeightR = 25
		} else {
			mainHeightR = 165
		}
		
		$(".emailRequestJs").each(function(i,elem) {
			var nameOfFurniturePreview = $(elem).html()
			var wid = screen.width, tSize = 0

	    	tSize = 40

	    	if (wid < 720) {
	    		tSize = 32
	    	}
    		
    		if (wid < 500) {
    			tSize = 22
    		}
	    	if (wid < 350) {
	    		tSize = 17
	    	}
			
			if (nameOfFurniturePreview.length > tSize) {
				$(elem).empty()
				$(elem).html(nameOfFurniturePreview.substr(0, tSize) + "...")
			}
		});
	}

	resizeOfFont()
	resizeOfFontR()

	function sleep(milliseconds) {
	  var start = new Date().getTime();
	  for (var i = 0; i < 1e7; i++) {
	    if ((new Date().getTime() - start) > milliseconds){
	      break;
	    }
	  }
	}

	var tt11 = false

	$(".areYouShureToDelete").toggle()

	$("#deleteRequestBtn").click(function(){
		$(".areYouShureToDelete").show()
		
		$(".formAreYouShure").css("margin-top", 50)
	  	$(".formAreYouShure").css("opacity", 0.2)
	  	$(".formAreYouShure").animate({"margin-top": "0px", "opacity": "1"}, 200);

		tt11 = true
	})

	$(".noBtn").click(function(){
		$(".areYouShureToDelete").toggle()
		tt11 = false
	})	

	$(".nativeMenu").css("display", "flex")
	$(".nativeMenu").toggle()	

	var trigger = true
	$( ".menuBtn1" ).click(function(){ 
		if (trigger) {
			if (!tr) {
				$(".nativeSearch").toggle()
				$("#searchBtn").each(function(i,elem) {
					$(elem).toggleClass('fa fa-close fa-lg').toggleClass('fa fa-search fa-lg');
				})	
				$(".f2gsx7766435fa").toggleClass('fa fa-close fa-lg').toggleClass('fa fa-search fa-lg');
				tr = true
			}

			if ($(".mainPageMarker").html() == "text") {
				if (window.pageYOffset < 170) {
					$(".menuBtn").css("color", "black")
					$(".menuBtn").css("box-shadow", "0 5px 10px rgb(0,0,0,0.3)")
					$(".f2gsx7766435fa").css("color", "black")
				}	
			}	

			if (tt11) {
		  		$(".areYouShureToDelete").toggle()
		  		tt11 = false
		  	}

		  	$(".nativeMenu").show()
		  	$(".nativeMenuWrap").css("padding-top", 50)
		  	$(".nativeMenuWrap").css("opacity", 0.2)
		  	$(".nativeMenuWrap").animate({"padding-top": "0px", "opacity": "1"}, 200);
			$('#navicon').toggleClass('fa fa-navicon fa-lg').toggleClass('fa fa-close fa-lg');
		  	trigger = false
		} else {
			if ($(".mainPageMarker").html() == "text") {
				if (window.pageYOffset < 170) {
					$(".menuBtn").css("color", "white")
					$(".menuBtn").css("box-shadow", "none")
					$(".f2gsx7766435fa").css("color", "white")
				}	
			}	

		  	$(".nativeMenuWrap").animate({"padding-top": "0px", "opacity": "0.2"}, 200);
			$(".nativeMenu").toggle()
		  	$('#navicon').toggleClass('fa fa-close fa-lg').toggleClass('fa fa-navicon fa-lg');
			trigger = true
		}
	});

	window.addEventListener('scroll', function() {
  		if ($(".mainPageMarker").html() == "text") {
			if (window.pageYOffset < 170) {
				if (!trigger) {
					$(".menuBtn").css("color", "black")
					$(".menuBtn").css("box-shadow", "0 5px 10px rgb(0,0,0,0.3)")
					$(".f2gsx7766435fa").css("color", "black")
				}	
			}	
		}
	});

	$(".nativeSearch").css("z-index", "9")
	$(".nativeSearch").toggle()
	
	var tr = true
	$(".search").click(function(){
		$("body").css("overflow", "hidden;")

		if (tr) {

			if (!trigger) {
				$(".nativeMenuWrap").animate({"padding-top": "100px", "opacity": "0.2"}, 200);
				$(".nativeMenu").toggle()
				$('#navicon').toggleClass('fa fa-close fa-lg').toggleClass('fa fa-navicon fa-lg');
				trigger = true

				if ($(".mainPageMarker").html() == "text") {
					if (window.pageYOffset < 170) {
						$(".menuBtn").css("color", "white")
						$(".menuBtn").css("box-shadow", "none")
						$(".f2gsx7766435fa").css("color", "white")
					}	
				}	
			}
		  	
		  	$("#searchBtn").toggleClass('fa fa-search fa-lg').toggleClass('fa fa-close fa-lg');
		  	$(".f2gsx7766435fa").toggleClass('fa fa-search fa-lg').toggleClass('fa fa-close fa-lg');

		  	// $("#searchBtn").toggleClass('fa fa-search fa-lg').toggleClass('fa fa-close fa-lg');
		  	 // $(".nativeSearch").css("backdrop-filter", "blur(1px)")
		  	$(".nativeSearch").css("padding-top", 40)
		  	$(".nativeSearch").css("opacity", 0.2)
		  	
		  	if (tt11) {
		  		$(".areYouShureToDelete").toggle()
		  		tt11 = false
		  	}
		  	
		  	$(".nativeSearch").show()
		  	$(".nativeSearch").animate({"padding-top": "30px", "opacity": "1"}, 0.001);

		  	tr = false
		
		} else {
			$(".nativeSearch").toggle()
			$("#searchBtn").each(function(i,elem) {
				$(elem).toggleClass('fa fa-close fa-lg').toggleClass('fa fa-search fa-lg');
			})
			$(".f2gsx7766435fa").toggleClass('fa fa-close fa-lg').toggleClass('fa fa-search fa-lg');
			tr = true
		}
	});
		
	if ($(".noname").html() == "hello") {			
		$(".search").css("display", "none")
	}
	
	scrollMenu()

	$(window).resize(function(){
		if (screen.width > 650 && !trigger) {
			$(".nativeMenu").toggle()
			
			if (tr) {
				$('#navicon').toggleClass('fa fa-navicon fa-lg').toggleClass('fa fa-close fa-lg');
			}	
			trigger = true
		}	

		resizeOfFont()
		resizeOfFontR()
		scrollMenu()
	});

});