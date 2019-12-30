$(document).ready(function(){
	$btnSearch = $(".search") 

	var trigger = true

    $btnSearch.click(function(){
    	if (trigger) {
        	$btnSearch.css({ "border-bottom": "3px solid #4400ff"})

        	$btnSearch.html()

    		trigger = false
    	} else {
    		$btnSearch.css({ "border-bottom": "none"})

    		trigger = true
    	}
    });
});