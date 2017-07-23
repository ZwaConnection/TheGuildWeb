$(document).ready(function(){
  console.log('Loaded');

  $('input#id_initials').change(function(){
      $('input#association_id').val($(this).val());
  });


  console.log($('input#association_id').val());
  // console.log($('input#identifier_id').val());
  //
  // $('#terms').click(function(){
  //   // check if the checkbox is checked
  //   if($(this).is(':checked')){
  //     $('#registerBtn').removeAttr('disabled');
  //   }else{
  //     $('#registerBtn').attr('disabled', 'disabled');
  //   }
  // });
  //
  $(function(){
    $('#id_year_of_creation').datepicker({ dateFormat: 'yy-mm-dd'});
  });

  $(function(){
    $('#id_dob').datepicker({dateFormat: 'yy-mm-dd'})
  });

});
