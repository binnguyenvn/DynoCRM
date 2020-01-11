$('.kt-select2').each(function(idx, el) {
    $(this).prepend($("<option></option>").attr("value", "").text("Select option"));
    $(this).select2({
        placeholder: "Select option"
    });
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