function SendMessage(num) {
    console.log(num)
    var name = $('#nameId').val();
    console.log(name)
    var email = $('#emailId').val();
    var subject = $('#subjectId').val();
    var message = $('#messageId').val();

    $.get('/add-message/', {
        name, email, subject, message
    }).then(res => {
        $('#resultId').html(res);
        $('#nameId').val('');
        $('#emailId').val('');
        $('#subjectId').val('');
        $('#messageId').val('');

    });
}