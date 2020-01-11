function load_widget() {
    $('.detailformsetdiv [id$="-external"]').select2({
        placeholder: 'External module'
    });
}

$.ajax({
    url: "/settings/apps/api/get_label",
    type: "GET",
    success: function(results) {
        $('#id_form-__prefix__-external').empty();
        $('#id_form-__prefix__-external').append($("<option></option>").attr("value", "").text(""));
        $.each(results.data, function(i, val) {
            $('#id_form-__prefix__-external').append($("<option></option>").attr("value", val.label).text(val.name));
        });
    }
});