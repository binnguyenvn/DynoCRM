function refreshField(name, url, which = 0) {
    $.ajax({
        url: url,
        type: "GET",
        success: function(results) {
            $('#id_' + name).empty();
            $('#id_' + name).append($("<option></option>").attr("value", "").text("------------"));
            $.each(results.data, function() {
                $('#id_' + name).append($("<option></option>").attr("value", this.id).text(this.value));
            });
            if (which == 0) {
                $('#id_' + name).val(results.data[0].id).change();
            }
        }
    });
}

$('.kt-select2').each(function(idx, el) {
    $(this).prepend($("<option></option>").attr("value", "").text("Select option"));
    $(this).select2({
        placeholder: "Select option"
    });
    if ($(this).is('[fk]')) {
        refreshField($(this).attr('name'), $(this).attr('refresh'), 1);
    }
});

$('.date-field').each(function(idx, el) {
    arrows = {
        leftArrow: '<i class="la la-angle-left"></i>',
        rightArrow: '<i class="la la-angle-right"></i>'
    }
    $(this).datepicker({
        todayHighlight: true,
        orientation: "bottom left",
        templates: arrows
    });
});
$('.datetime-field').each(function(idx, el) {
    $(this).datetimepicker({
        todayHighlight: true,
        autoclose: true,
        format: 'yyyy.mm.dd hh:ii'
    });
});
$('.time-field').each(function(idx, el) {
    $(this).timepicker();
});