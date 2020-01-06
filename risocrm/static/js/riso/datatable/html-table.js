(function($, window, document, undefined) {

    "use strict";
    var pluginName = "risoHtmlTable",
        defaults = {
            tableSelector: '',
            rowGroup: {
                dataSrc: []
            },
            columnIndex: {
                targets: 0,
                orderable: false,
                render: function(data, type, full, meta) {
                    return `
                <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid">
                    <input type="checkbox" value="" data-record=${data} class="kt-checkable">
                    <span></span>
                </label>`;

                },
            }
        };

    function Plugin(element, options) {
        this.element = element;

        this.settings = $.extend({}, defaults, options);
        this._defaults = defaults;
        this._name = pluginName;
        this.init();
    }

    $.extend(Plugin.prototype, {
        init: function() {
            var that = this;
            var settings = that.settings;

            var table = $(that.element);

            settings.table = table;

            that.tableOptions = {
                select: {
                    style: 'multi',
                    selector: 'td:first-child .kt-checkable',
                },
                headerCallback: function(thead, data, start, end, display) {
                    thead.getElementsByTagName('th')[0].innerHTML = `
                        <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid">
                            <input type="checkbox" value="" class="kt-group-checkable">
                            <span></span>
                        </label>`;
                },
                order: [
                    [1, "asc"]
                ],
                columnDefs: [
                    settings.columnIndex,
                    {
                        targets: settings.rowGroup.dataSrc,
                        visible: false
                    }
                ]
            };
            if (settings.rowGroup.dataSrc.length > 0) {
                that.tableOptions.rowGroup = settings.rowGroup;
            }
            this.initTable();

            table.on('change', '.kt-group-checkable', function() {
                var set = $(this).closest('table').find('td:first-child .kt-checkable');
                var checked = $(this).is(':checked');

                $(set).each(function() {
                    if (checked) {
                        $(this).prop('checked', true);
                    } else {
                        $(this).prop('checked', false);
                    }
                });
            });

        },

        initTable: function() {

            var that = this;
            var settings = that.settings;
            var options = that.tableOptions;

            settings.table.dataTable(options);
        },

        getSelectedRow: function() {
            var settings = this.settings;
            var ids = '';

            settings.table.find('td:first-child .kt-checkable:checked').map(function(_index, element) {
                var val = $(element).data('record');
                ids += val + ',';
            });

            return ids;
        }
    });

    $.fn[pluginName] = function(options) {
        return this.each(function() {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" +
                    pluginName, new Plugin(this, options));
            }
        });
    };

})(jQuery, window, document);