function load_widget() {
    $('.detailformsetdiv [id$=-field]').select2({
        placeholder: 'Select Field'
    });
}

function moduleDefault(value) {
    $('#id_form-__prefix__-module').val(value);
}