"use strict"

$(window).on("load", function() {
    $('.btn-forget').on('click',function(e){
        e.preventDefault();
        var inputField = $(this).closest('form').find('input');
        if(inputField.attr('required') && inputField.val()){
            $('.error-message').remove();
            $('.form-items','.form-content').addClass('hide-it');
            $('.form-sent','.form-content').addClass('show-it');
        }else{
            $('.error-message').remove();
            $('<small class="error-message">Please fill the field.</small>').insertAfter(inputField);
        }

    });
    
    $('.btn-tab-next').on('click',function(e){
        e.preventDefault();
        $('.nav-tabs .nav-item > .active').parent().next('li').find('a').trigger('click');
    });
    $('.custom-file input[type="file"]').on('change', function(){
        var filename = $(this).val().split('\\').pop();
        $(this).next().text(filename);
    });
});

$(document).ready(function() {
    // Başlangıçta tüm alanları gizle
    $('#tckn-group').hide();
    $('#passport-group').hide();

    // Kullanıcı tipi seçildiğinde alanları göster/gizle
    $('#id_user_type').change(function() {
        var selectedType = $(this).val();
        toggleFields(selectedType);
    });

    // Sayfa yüklendiğinde mevcut kullanıcı tipi seçeneğine göre alanları göster/gizle
    var userType = $('#id_user_type').val();
    if (userType) {
        toggleFields(userType);
    }

    function toggleFields(type) {
        if (type === 'Turkish') {
            $('#tckn-group').show();
            $('#passport-group').hide();
            $('#id_tckn').attr('required', true);
            $('#id_passport_number').attr('required', false);
        } else if (type === 'Foreign') {
            $('#tckn-group').hide();
            $('#passport-group').show();
            $('#id_tckn').attr('required', false);
            $('#id_passport_number').attr('required', true);
        } else {
            $('#tckn-group').hide();
            $('#passport-group').hide();
            $('#id_tckn').attr('required', false);
            $('#id_passport_number').attr('required', false);
        }
    }
});