// Example

var Accordion = {
    Elements: {
        titles: $('h3', 'div.accordion')
    },

    print: function(option){
        		alert(option);
    },

    Events: {
        
        open: function(evt) {
            if (evt.data.element.is(':hidden')) {
                evt.data.element.slideDown(600);
            } else {

                this.close();

            }
        },
        close: function(evt) {

            if (evt.data.element.is(':visible')) {
                evt.data.element.slideUp(600);

            } else {

                this.open();

            }
        },
        bind: function() {

            Accordion.Elements.titles.each(function() {

                var $header = $(this);
                var $content = $header.next();

                $header.bind('open', {
                    element: $content
                }, Accordion.Events.open);
                $header.bind('close', {
                    element: $content
                }, Accordion.Events.close);

            });

        }
    },
    
    fn: {
        
        attachEvents: function() {
            
            Accordion.Events.bind();
 
            Accordion.Elements.titles.on('click', function() {
                
                $('div.accordion-content').slideUp(600);
                $(this).trigger('open');

            });                
            
            
        }
    },
    
    init: function() {
        
        Accordion.fn.attachEvents();
    }
};


Accordion.init();

