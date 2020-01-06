$('#id_module').select2({
    placeholder: "Select Module",
});
$('#id_width').select2({
    placeholder: "Select width"
});
$('#id_dashboard').select2({
    placeholder: "Group of Tile",
});
$('#id_type').select2({
    placeholder: "Type of Chart",
});
$('#id_field').select2({
    placeholder: "Select category field",
});

function load_widget() {
    $('.detailformsetdiv [id$="-field"]').select2({
        placeholder: 'Field name'
    });

    $('.detailformsetdiv [id$="-type"]').select2({
        placeholder: 'Type of field'
    });
}

$('#id_module').on('change', function() {
    $.ajax({
        url: "/settings/apps/api/get_field?model=" + this.value,
        type: "GET",
        success: function(results) {
            $('.detailformsetdiv [id$="-field"]').empty();
            $('#id_field').empty();
            $('.detailformsetdiv [id$="-field"]').append($("<option></option>").attr("value", "").text(""));
            $('#id_field').append($("<option></option>").attr("value", "").text(""));
            $.each(results.data, function(i, val) {
                $('.detailformsetdiv [id$="-field"]').append($("<option></option>").attr("value", val.val).text(val.name));
                $('#id_field').append($("<option></option>").attr("value", val.val).text(val.name));
            });
        }
    });
});