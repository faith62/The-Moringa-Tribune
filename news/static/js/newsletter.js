$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
          //create the AJAX request.
      $.ajax({
        'url':'/ajax/newsletter/',
        'type':'POST',
        'data':form.serialize(), // passing to the request.
        'dataType':'json', //converts the form values into a JSON 
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_your_name').val('') // clear the form fields. 
      $("#id_email").val('')
  
        

    }) // End of submit event
  
  }) // End of document ready function