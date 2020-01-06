"use strict";

var showErrorMsg = function(form, type, msg) {
    var alert = $('<div class="alert alert-bold alert-solid-' + type + ' alert-dismissible" role="alert">\
		<div class="alert-text">' + msg + '</div>\
		<div class="alert-close">\
			<i class="flaticon2-cross kt-icon-sm" data-dismiss="alert"></i>\
		</div>\
	</div>');

    form.find('.alert').remove();
    alert.prependTo(form);
    KTUtil.animateClass(alert[0], 'fadeIn animated');
}