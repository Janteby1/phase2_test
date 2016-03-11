$(document).ready(function(){
  console.log("Hi there!")

    $('.wcards_button').on('submit', function(event){
    event.preventDefault();

    console.log ("clicked!"); //for testing 

    $.ajax({
        method: "GET",
        url: ("/cards/white"), //just goest to url  
        success: function(data){
            console.log("here"); //for testing 

            console.log (data) // for testing 
            // use this to just stick it onto the DOM
            // $('.wcard_div').append(data.cards)
            
            var template = $('#list').html();
            // we get an object with a property comments, so here we call data.comments or just pass the data
            var renderM = Mustache.render(template,data);
            console.log(renderM); //for testing 

            $(".wcard_div").html(renderM) // just attach it to post adn we dont need to conditional 
                
            }
        })
    })
/////////////////////       ////////////////////         /////////////////////


    $('.bcards_button').on('submit', function(event){
	event.preventDefault();

	console.log ("clicked!"); //for testing 

	$.ajax({
        method: "GET",
        url: ("/cards/black"), //just goest to url  
        success: function(data){
        	console.log("here"); //for testing 

            console.log (data) // for testing 
            // use this to just stick it onto the DOM
            // $('.bcard_div').text(data.cards)

            var template = $('#list').html();
			// we get an object with a property comments, so here we call data.comments or just pass the data
			var renderM = Mustache.render(template,data);
			console.log(renderM); //for testing 

			$(".bcard_div").html(renderM) // just attach it to post adn we dont need to conditional 
                
			}
		})
	})
});

