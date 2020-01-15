function sentenceCase(str) {
    if ((str === null) || (str === ''))
        return false;
    else
        str = str.toString();

    return str.replace(/\w\S*/g,
        function(txt) {
            return txt.charAt(0).toUpperCase() +
                txt.substr(1).toLowerCase();
        });
}

(function($, window, document, undefined) {

    "use strict";
    var pluginName = "risoDynamicTable",
        defaults = {
            baseUrl: "",
            tableSelector: '',
            columnIndex: {
                targets: 1,
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
                targets: 0,
                title: 'Actions',
                orderable: false,
                render: function(data, type, full, meta) {
                    return '';
                }
            },
            columnImage: {

            },
            columnChoice: {

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
                columns: [],
                select: {
                    style: 'multi',
                    selector: 'td:first-child .kt-checkable',
                },
                responsive: true,
                headerCallback: function(thead, data, start, end, display) {
                    thead.getElementsByTagName('th')[1].innerHTML = `
                        <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid">
                            <input type="checkbox" value="" class="kt-group-checkable">
                            <span></span>
                        </label>`;
                },
                columnDefs: [
                    settings.columnIndex,
                    settings.columnAction,
                    settings.columnImage,
                    settings.columnChoice

                ]
            };

            if (settings.baseUrl) {
                this.filterTable(settings.baseUrl);

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
            } else {
                console.log('Must have baseurl and tableSelector');
            }
        },

        setAutoColumns: function(kw) {
            var that = this;
            var options = that.tableOptions;
            options.columns.push({});
            $.each(that.dataSet[0], function(k, v) {
                var found = $.grep(options.columns, function(n, i) {
                    return k === n.data;
                });
                if (found.length === 0) {
                    var title = (typeof kw[k] == 'undefined') ? sentenceCase(k) : kw[k];
                    options.columns.push({ data: k, title: title });
                }
            });
        },

        filterTable: function(url) {
            var that = this;
            var settings = that.settings;
            var options = that.tableOptions;
            $.ajax('/settings/apps/api/get_field_label').then(function(res) {
                $.ajax(url + '&start=0&length=10').then(function(r) { // Initial Columns
                    var data = r.data;
                    that.dataSet = data;
                    that.setAutoColumns(res.data);
                    options.ajax = url;
                    options.processing = true;
                    options.serverSide = true;
                    settings.table.dataTable(options);
                });
            });

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