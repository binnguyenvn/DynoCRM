"use strict";

// Daterangepicker Init
var daterangepickerInit = function() {
    if ($('#kt_dashboard_daterangepicker').length == 0) {
        return;
    }

    var picker = $('#kt_dashboard_daterangepicker');
    var start = moment();
    var end = moment();

    function cb(start, end, label) {
        var title = '';
        var range = '';

        if ((end - start) < 100 || label == 'Today') {
            title = 'Today:';
            range = start.format('MMM D');
        } else if (label == 'Yesterday') {
            title = 'Yesterday:';
            range = start.format('MMM D');
        } else {
            range = start.format('MMM D') + ' - ' + end.format('MMM D');
        }

        $('#kt_dashboard_daterangepicker_date').html(range);

        $('#kt_dashboard_daterangepicker_date_start').val(start.format('YYYY-MM-DD'));
        $('#kt_dashboard_daterangepicker_date_end').val(end.format('YYYY-MM-DD')).change();

        $('#kt_dashboard_daterangepicker_title').html(title);
    }

    picker.daterangepicker({
        direction: KTUtil.isRTL(),
        startDate: start,
        endDate: end,
        opens: 'left',
        ranges: {
            'Today': [moment(), moment()],
            'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);

    //cb(start, end, '');
    var title = 'Today:';
    var range = start.format('MMM D');
    $('#kt_dashboard_daterangepicker_date').html(range);
    $('#kt_dashboard_daterangepicker_title').html(title);
}