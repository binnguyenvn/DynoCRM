(function($, window, document, undefined) {

    "use strict";
    var pluginName = "risoFixedTable",
        defaults = {
            tableSelector: '',
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
            },
            columnAction: {
                targets: -1,
                title: 'Actions',
                orderable: false,
                render: function(data, type, full, meta) {
                    return '';
                }
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

            that.dataSet = settings.data;

            settings.table = table;

            that.tableOptions = {
                columns: [],
                select: {
                    style: 'multi',
                    selector: 'td:first-child .kt-checkable',
                },
                responsive: true,
                headerCallback: function(thead, data, start, end, display) {
                    thead.getElementsByTagName('th')[0].innerHTML = `
                        <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid">
                            <input type="checkbox" value="" class="kt-group-checkable">
                            <span></span>
                        </label>`;
                },
                columnDefs: [
                    settings.columnIndex,
                    settings.columnAction
                ]
            };

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

            options.data = settings.data;
            that.setAutoColumns();

            settings.table.dataTable(options);
        },

        setAutoColumns: function() {
            var that = this;
            var options = that.tableOptions;
            $.each(that.dataSet[0], function(k, v) {
                var found = $.grep(options.columns, function(n, i) {
                    return k === n.data;
                });
                if (found.length === 0) {
                    options.columns.push({ data: k, title: k });
                }
            });
            options.columns.push({});

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