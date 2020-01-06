$('#id_type').select2({
    placeholder: "Select type"
});
$('#id_group').select2({
    placeholder: "Select Group",
    tags: true
});
$('#id_module').select2({
    placeholder: "Select module"
});

$(document).delegate('#id_option', 'change', function(e) {
    $.ajax({
        url: '/settings/choices/api/choice_childs/' + $('#id_option').val(),
        type: "GET",
        success: function(results) {
            $('#id_default').empty();
            $('#id_default').append($("<option></option>").attr("value", "").text("------------"));
            $.each(results.data, function() {
                $('#id_default').append($("<option></option>").attr("value", this.id).text(this.value));
            });
            var curr = $('#id_default_val').val();
            $('#id_default').val(curr).change();
        }
    });

});

var $formContainer = $('#form-container');
var listFieldObjects = {
    ForeignKey: ['fkmodule', 'ondelete', ],
    ManyToManyField: ['fkmodule', 'ondelete', ],
    OneToOneField: ['fkmodule', 'ondelete', ],

    CharField: ['option', 'detail', 'maxlength'],
    TextField: ['default', ],

    BooleanField: ['default', ],
    NullBooleanField: ['default', ],

    DateField: [],
    DateTimeField: [],
    TimeField: [],

    BigIntegerField: ['default', ],
    IntegerField: ['default', ],
    PositiveIntegerField: ['default', ],
    PositiveSmallIntegerField: ['default', ],
    SmallIntegerField: ['default', ],
    DecimalField: ['default', ],
    FloatField: ['default', ],

    FileField: ['maxlength', ],
    ImageField: ['maxlength', ]
};

function field_render() {
    $formContainer.empty().change();
    var listFormControl = listFieldObjects[$('#id_type').val()];

    if (listFormControl) {
        listFormControl.forEach(function(control) {
            var template = $('#hbs-' + control);
            if (template) {
                $formContainer.append(template.html()).change();
            }
            if (control == 'fkmodule') {
                $('#id_fkmodule').select2({
                    placeholder: "Select ForeignKey Module"
                }).change();
            }
            if (control == 'ondelete') {
                $('#id_on_delete').select2({
                    placeholder: "Select On delete"
                }).change();
            }
            if (control == 'option') {
                $('#id_option').select2({
                    placeholder: "Select Choice"
                }).change();
            }
        });
        switch ($('#id_type').val()) {
            case 'ForeignKey':
            case 'ManyToManyField':
            case 'OneToOneField':
                $('#id_default').select2({
                    placeholder: 'Select default'
                }).change();
                break;
            case 'TextField':
                input = '<input type="text" step="any" name="default" class="form-control" maxlength="500" id="id_default" placeholder="Enter default value"></input>';
                $("#id_default").replaceWith(input).change();
                break;
            case 'CharField':
                $('#id_default').select2({
                    placeholder: 'Select default'
                }).change();
                break;
            case 'BooleanField':
            case 'NullBooleanField':
                $('#id_default').append($("<option></option>").attr("value", "").text("")).change();
                $('#id_default').append($("<option></option>").attr("value", "True").text("True")).change();
                $('#id_default').append($("<option></option>").attr("value", "False").text("False")).change();
                $('#id_default').select2({
                    placeholder: 'Select default'
                }).change();
                break;
            case 'BigIntegerField':
            case 'IntegerField':
            case 'SmallIntegerField':
            case 'PositiveIntegerField':
            case 'PositiveSmallIntegerField':
            case 'DecimalField':
            case 'FloatField':
                input = '<input type="number" step="any" name="default" class="form-control" maxlength="500" id="id_default" placeholder="Enter default number"></input>';
                $("#id_default").replaceWith(input).change();
                break;
            default:
                break;
        }

    }
}

$('[data-input-type]').on('change', 'select', function(e) {
    field_render();
});

$(document).ready(function() {
    if ($('#id_type').val() != '') {
        field_render();
    }
});