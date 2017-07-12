$(document).ready(function(){
  console.log('Loaded');

  $('#id_initials').change(function(){
      $('#id_username').val($(this).val());
  });

  $('#terms').click(function(){
    // check if the checkbox is checked
    if($(this).is(':checked')){
      $('#registerBtn').removeAttr('disabled');
    }else{
      $('#registerBtn').attr('disabled', true);
    }
  });




});
