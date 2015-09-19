$(document).ready(function() {
  $.getScript("static/js/controllers/util.js", function() { // "util.js" can be changed as you wish. ex) auth.js

  	// Example
  	var a = Accordion;
  	a.print("Hello");
  	
     $('h3', 'div.accordion').each(function() {

            var $header = $(this);
            var $content = $header.next();
            
            $header.click(function() {
            
                $('div.accordion-content').slideUp(600); // hide all contents
                             
            
            });

        });
	});
});
