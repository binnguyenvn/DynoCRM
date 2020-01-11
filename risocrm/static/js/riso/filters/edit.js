function render_field() {
    $.ajax({
        url: "/settings/apps/api/get_field?model=" + $('#id_module').val(),
        type: "GET",
        success: function(results) {
            $('#id_field_list').empty();
            $('#id_order_by').empty();
            $('#id_filter_details-__prefix__-field_name').empty();
            $('.detailformsetdiv [id$="-field_name"]').empty();
            $('#id_field_list').append($("<option></option>").attr("value", "").text(""));
            $('#id_order_by').append($("<option></option>").attr("value", "").text(""));
            $('#id_filter_details-__prefix__-field_name').append($("<option></option>").attr("value", "").text(""));
            $('.detailformsetdiv [id$="-field_name"]').append($("<option></option>").attr("value", "").text(""));
            $.each(results.data, function(i, val) {
                $('#id_field_list').append($("<option></option>").attr("value", val.val).text(val.name));
                $('#id_order_by').append($("<option></option>").attr("value", val.val).text(val.name));
                $('#id_filter_details-__prefix__-field_name').append($("<option></option>").attr("value", val.val).text(val.name));
                $('.detailformsetdiv [id$="-field_name"]').append($("<option></option>").attr("value", val.val).text(val.name));
            });
        }
    });
}

$('#id_module').on('change', function() {
    render_field();
});


function changeFieldInput(callback = function(form) {}) {
    $(document).delegate('.field-name', 'change', function(e) {
        var form = $(e.target).parents('.contain_form');
        var idx = $(this)[0].id.split('-')[1];
        var module = $('#id_module').val();
        var field = $(this).val();
        $.ajax({
            url: "/settings/apps/api/get_field_type?model=" + module + "&field=" + field,
            type: "GET",
            success: function(results) {
                $('#id_div_filter_details-' + idx + '-value').empty();
                var arrows = {
                    leftArrow: '<i class="la la-angle-left"></i>',
                    rightArrow: '<i class="la la-angle-right"></i>'
                };
                switch (results.data) {
                    case 'ForeignKey':
                    case 'ManyToManyField':
                    case 'OneToOneField':
                        var input = `
                            <select class="field-value form-control kt-select2" name="filter_details-` + idx + `-value" id="id_filter_details-` + idx + `-value">
                            </select>`;

                        $('#id_div_filter_details-' + idx + '-value').append(input);

                        $.ajax({
                            url: "/settings/apps/api/get_foreign_data?model=" + module + "&field=" + field,
                            type: "GET",
                            success: function(results) {
                                $.each(results.data, function(i, val) {
                                    var text = '';
                                    if (val.value) {
                                        text = val.value;
                                    }
                                    if (val.name) {
                                        text = val.name;
                                    }
                                    if (val.first_name) {
                                        text = val.first_name;
                                    }

                                    $('#id_filter_details-' + idx + '-value').append($("<option></option>").attr("value", val.id).text(text));
                                });
                                $('#id_filter_details-' + idx + '-value').select2({
                                    placeholder: 'Select option'
                                });
                            },
                            error: function(results) {
                                $('#id_filter_details-' + idx + '-value').select2({
                                    placeholder: 'Select option'
                                });
                            },
                        });
                        break;
                    case 'TextField':
                    case 'CharField':
                    case 'UUIDField':
                        input = '<input type="text" name="filter_details-' + idx + '-value" class="field-value form-control" maxlength="500" id="id_filter_details-' + idx + '-value"></input>';
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-field_type').val('str').prop('selected', true).change();
                        break;
                    case 'BooleanField':
                    case 'NullBooleanField':
                        input = `
                        <select class="field-value form-control kt-select2" name="filter_details-` + idx + `-value" id="id_filter_details-` + idx + `-value">
                            <option></option>
                            <option value="true">True</option>
                            <option value="false">False</option>
                        </select>
                        `;
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-value').select2({
                            placeholder: 'Select option'
                        });
                        $('#id_filter_details-' + idx + '-field_type').val('str').prop('selected', true).change();
                        break;
                    case 'DateField':
                        input = `
                            <div class="input-group date">
                                <input type="text" class="field-value form-control" readonly name="filter_details-` + idx + `-value" id="id_filter_details-` + idx + `-value" />
                                <div class="input-group-append">
                                    <span class="input-group-text">
                                        <i class="la la-calendar"></i>
                                    </span>
                                </div>
                            </div>
                        `;
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-value').datepicker({
                            rtl: KTUtil.isRTL(),
                            todayBtn: "linked",
                            clearBtn: true,
                            todayHighlight: true,
                            templates: arrows
                        });
                        $('#id_filter_details-' + idx + '-field_type').val('str').prop('selected', true).change();
                        break;
                    case 'DateTimeField':
                        input = `
                        <div class="input-group date">
                            <input type="text" class="field-value form-control" readonly name="filter_details-` + idx + `-value" id="id_filter_details-` + idx + `-value" />
                            <div class="input-group-append">
                                <span class="input-group-text">
                                    <i class="la la-calendar"></i>
                                </span>
                            </div>
                        </div>
                        `;
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-value').datetimepicker({
                            todayHighlight: true,
                            autoclose: true,
                            pickerPosition: 'bottom-left',
                            todayBtn: true,
                            format: 'yyyy/mm/dd hh:ii'
                        });
                        $('#id_filter_details-' + idx + '-field_type').val('str').prop('selected', true).change();
                        break;
                    case 'TimeField':
                        input = `
                            <div class="input-group timepicker">
                                <input class="field-value form-control" readonly placeholder="Select time" type="text" name="filter_details-` + idx + `-value" id="id_filter_details-` + idx + `-value" />
                                <div class="input-group-append">
                                    <span class="input-group-text">
                                        <i class="la la-clock-o"></i>
                                    </span>
                                </div>
                            </div>
                        `;
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-value').timepicker({
                            minuteStep: 1,
                            defaultTime: '',
                            showSeconds: true,
                            showMeridian: false,
                            snapToStep: true
                        });
                        $('#id_filter_details-' + idx + '-field_type').val('str').prop('selected', true).change();
                        break;
                    case 'BigIntegerField':
                    case 'IntegerField':
                    case 'SmallIntegerField':
                        input = '<input type="number" name="filter_details-' + idx + '-value" class="field-value form-control" maxlength="500" id="id_filter_details-' + idx + '-value"></input>';
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-field_type').val('int').prop('selected', true).change();
                        break;
                    case 'PositiveIntegerField':
                    case 'PositiveSmallIntegerField':
                        input = '<input type="number" min="0" name="filter_details-' + idx + '-value" class="field-value form-control" maxlength="500" id="id_filter_details-' + idx + '-value"></input>';
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-field_type').val('int').prop('selected', true).change();
                        break;
                    case 'DecimalField':
                    case 'FloatField':
                        input = '<input type="text" step="any" name="filter_details-' + idx + '-value" class="field-value form-control" maxlength="500" id="id_filter_details-' + idx + '-value"></input>';
                        $('#id_div_filter_details-' + idx + '-value').append(input);
                        $('#id_filter_details-' + idx + '-field_type').val('int').prop('selected', true).change();
                        break;
                    default:
                        break;
                }
            }
        });

        callback(form);
    });
}

function changeOperatorInput(callback = function(form) {}) {
    $(document).delegate('.field-operator', 'change', function(e) {

        var form = $(e.target).parents('.contain_form');
        var idx = $(this)[0].id.split('-')[1];

        var field = $(this).val();
        if (field == 'in') {

            $('#id_title-' + idx).text('Use Comma "," to separate item!');
            if ($('#id_filter_details-' + idx + '-value').prop('type') == 'select-one') {

                $('#id_filter_details-' + idx + '-value').attr('multiple', '');
                $('#id_filter_details-' + idx + '-value').select2({
                    placeholder: "Select multiple",
                });
                $('#id_filter_details-' + idx + '-value').attr('id', 'id_filter_details-' + idx + '-value-fake');
                input = '<input type="text" name="filter_details-' + idx + '-value" class="field-value form-control" maxlength="500" id="id_filter_details-' + idx + '-value" hidden></input>';
                $('#div-next-' + idx + '-HIDDEN').append(input);
                var nvar = '';
                $.each($('#id_filter_details-' + idx + '-value-fake').val(), function(k, v) {
                    nvar += v + ',';
                });
                $('#id_filter_details-' + idx + '-value').val(nvar);
            }
        }
        callback(form);
    });
}

function changeValueInput(callback = function(form) {}) {
    $(document).delegate('.field-value', 'change', function(e) {
        var form = $(e.target).parents('.contain_form');
        var idx = $(this)[0].id.split('-')[1];
        var val = $('#id_filter_details-' + idx + '-value-fake').val();
        var nvar = '';
        $.each($('#id_filter_details-' + idx + '-value-fake').val(), function(k, v) {
            nvar += v + ',';
        });
        $('#id_filter_details-' + idx + '-value').val(nvar);
        callback(form);
    });
}

function load_widget() {
    $('.detailformsetdiv [id$="-field_name"]').select2({
        placeholder: 'Field name to compare'
    });

    $('.detailformsetdiv [id$="-operator"]').select2({
        placeholder: 'Compare operator'
    });

    $('.detailformsetdiv [id$="-next"]').select2({

    });
}

$(document).ready(function() {
    $('.detailformsetdiv input[id$="-value"]').each(function(idx, el) {
        if (el.value.includes(',')) {
            var val = el.value;
            $('#id_filter_details-' + idx + '-field_name').change();
            setTimeout(function() {
                $('#id_filter_details-' + idx + '-value').attr('multiple', '');
                $('#id_filter_details-' + idx + '-value').select2({
                    placeholder: "Select multiple",
                });
                $('#id_filter_details-' + idx + '-value').attr('id', 'id_filter_details-' + idx + '-value-fake');
                input = '<input type="text" name="filter_details-' + idx + '-value" class="field-value form-control" maxlength="500" id="id_filter_details-' + idx + '-value" hidden></input>';
                $('#div-next-' + idx + '-HIDDEN').append(input);
                $('#id_filter_details-' + idx + '-value-fake').val(val.split(',')).change();
            }, 100);
        }
    });
});