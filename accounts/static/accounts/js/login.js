$(document).on('submit', '#id_login', function (e) {

    e.preventDefault();
    let login_form = $('#id_login');
    let action = login_form.attr('action');
    let method = login_form.attr('method');
    let data_ = login_form.serialize();

    $.ajax({
        type: method,
        url: action,
        data: data_,
        success: function (data, status) {
            if ($(data).find('.text-danger').length > 0) {
                $('#modal .modal-content').html(data);
            } else {
                $('#modal').modal('hide');
                location.assign('/destinations/'); //Reload the current document page on success
            }
        }
    });
    return false;
});