function get_counter() {
    $.ajax({
        url: "/settings/notices/api/unread_count",
        type: "GET",
        success: function(results) {
            if (results.unread > 0) {
                $('#id_notice_counter').text(results.unread);
            }
        }
    });
}
//Definition of the function (non-global, because of the previous line)
function get_notices() {
    $.ajax({
        url: "/settings/notices/api/get_list",
        type: "GET",
        success: function(results) {
            $("#id_notice_panel").empty();
            $.each(results.data, function(i, notice) {
                content = `<a href="javascript:;" class="kt-notification__item `
                if (notice.is_read == true) {
                    content += 'kt-notification__item--read'
                }
                content += `" data-item="` + notice.id + `">
                  <div class="kt-notification__item-icon">
                      <i class="` + notice.type + ` kt-font-primary"></i>
                  </div>
                  <div class="kt-notification__item-details">
                      <div class="kt-notification__item-title">
                          ` + notice.content + `
                      </div>
                      <div class="kt-notification__item-time">
                          ` + $.timeago(notice.time_created) + `
                      </div>
                  </div>
              </a>
            `
                $("#id_notice_panel").append(content);
            });
        }
    });
}

$(document).delegate('.kt-notification__item', 'click', function(e) {
    $.ajax({
        url: "/settings/notices/api/reading/" + $(this).data('item'),
        type: "GET",
        success: function(results) {
            if (results.data != '') {
                window.location.replace("/" + results.data);
            }
        }
    });

});