$(document).ready(function(){
  console.log('Loaded');

  $('#id_initials').change(function(){
      $('#id_username').val($(this).val());
  });

  console.log($('#id_username').val());



});
