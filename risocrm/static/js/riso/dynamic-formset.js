function addFormSet(callback = function(form) {}) {
    $(document).delegate('.addBtnDetailFS', 'click', function(e) {
        var form = $(e.target).parents('.contain_form');
        var form_idx = form.find('[id$="-TOTAL_FORMS"]').val();
        var element = form.find('.nullDivDetail').html().replace(/__prefix__/g, form_idx);
        form.find('.detailformsetdiv').append(element);
        form.find('[id$="-TOTAL_FORMS"]').val(parseInt(form_idx) + 1);
        form.find('[id$="-HIDDEN"]').each(function(i, val) {
            if (i < form.find('[id$="-HIDDEN"]').length - 2) {
                $(this).removeClass('d-none');
            }
        });
        callback(form);
    });
}

function deleteFormSet(callback = function(form) {}) {
    $(document).delegate('.btn-delete-item', 'click', function(e) {
        var form = $(e.target).parents('.contain_form');
        var item_idx = $(this).data('item');
        form.find(".rowDetail-" + item_idx).addClass('d-none');
        form.find('div[class*="rowDetail"]div:not(.d-none)').each(function(i, val) {
            if (i == form.find('div[class*="rowDetail"]div:not(.d-none)').length - 2) {
                $(this).find('[id$="-HIDDEN"]').addClass('d-none');
            }
        });
        callback(form);
    });
}