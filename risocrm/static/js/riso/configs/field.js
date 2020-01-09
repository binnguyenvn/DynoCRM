function load_widget() {
    $('.detailformsetdiv [id$=-field]').select2({
        placeholder: 'Select Field'
    });
    $('.detailformsetdiv [id$=-module]').each(function(idx, el) {
        $('#id_form-' + idx + '-module').val($('#id_form-__prefix__-module').val());
        $('#id_form-' + idx + '-creator').val($('#id_form-__prefix__-creator').val());
        $('#id_form-' + idx + '-last_modified_by').val($('#id_form-__prefix__-last_modified_by').val());
        console.log($('#id_form-' + idx + '-module').val());
    });

}

function moduleDefault(value) {
    $('#id_form-__prefix__-module').val(value);
}

function initPage(module) {
    $.ajax({
        url: "/settings/apps/api/get_field?model=" + module,
        type: "GET",
        success: function(results) {
            $('#id_form-__prefix__-field').empty();
            $('#id_form-__prefix__-field').append($("<option></option>").attr("value", "").text(""));
            $.each(results.data, function(i, val) {
                $('#id_form-__prefix__-field').append($("<option></option>").attr("value", val.val).text(val.name));
            });
        }
    });
}