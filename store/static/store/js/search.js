$(document).ready(function(){
	$btnSearch = $(".search") 
	$searchWrap = $(".search-wrap")

	var trigger = true	

    $btnSearch.click(function(){
    	if (trigger) {
        	$btnSearch.css({ "border-bottom": "3px solid #4400ff"})

    		$searchWrap.html()

    		trigger = false

    	} else {
    		$btnSearch.css({ "border-bottom": "none"})

    		$searchWrap.empty();

    		trigger = true
    	}
    })

});