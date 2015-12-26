

$('#button_add').click(
    function(){
        $('.prod_form:visible:last').next(':hidden:first').css('display', '');
    });