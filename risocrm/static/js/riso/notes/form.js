function notePull() {
    $.ajax({
        url: "{% url 'notes:contacts-list' %}",
        type: "GET",
        success: function(results) {
            $.each(results.data, function() {
                var input = `
                <div class="kt-notes__item">
                    <div class="kt-notes__media">
                        <span class="kt-notes__icon">
                            <i class="` + this.type + ` kt-font-danger"></i>
                        </span>
                    </div>
                    <div class="kt-notes__content">
                        <div class="kt-notes__section">
                            <div class="kt-notes__info">
                                <a href="#" class="kt-notes__title">
                                    ` + this.creator.first_name + `
                                </a>
                                <span class="kt-notes__desc">
                                    ` + this.time_created + `
                                </span>
                            </div>
                        </div>
                        <span class="kt-notes__body">
                            ` + this.note + `
                        </span>
                    </div>
                </div>
                `;
                $('#id_noteScroll').append(input);
            });
        }
    });
}
notePull();