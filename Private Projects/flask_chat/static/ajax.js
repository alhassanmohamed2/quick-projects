 setInterval(function() {
     chat_update();
 }, 1000)


 $(document).on('click', '.send', function() {

     var chat_message = $.trim($('.msg').val());
     $.ajax({
         url: "/send",
         method: "POST",
         data: {
             msg: chat_message
         },
         success: function(data) {
             $('.msg').val('')

         }
     })

 })


 $(document).on('click', '.delete', function() {

     $.ajax({
         url: "/delete",
         method: "POST"
     })

 })

 function chat_update() {
     $.ajax({
         url: "/chat_update",
         method: "POST",
         success: function(data) {
             $('.chat').html(data);
         }
     })
 }



 if (window.history.replaceState) {
     window.history.replaceState(null, null, window.location.href)
 }