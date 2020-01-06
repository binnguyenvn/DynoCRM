function ajax_get(url) {
    $.ajax({
        url: url,
        type: "GET",
        success: function(results) {
            alert(results.data)
        }
    });
}