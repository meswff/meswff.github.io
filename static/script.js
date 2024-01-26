function show() {
    element = document.querySelector('other_div')
    element.style.visibility = 'visible';;
  }

function saveFormData() {
    // Get selected status value
    var selectedStatus = document.getElementById("statusSelect").value;

    // Get date/time and comments
    var localDate = document.getElementById("localdate").value;
    var comments = document.getElementById("name").value;

    var lead_id = document.location.pathname
    var lead_id = lead_id.substring(1);

    // Create a data object
    var formData = {
        status: selectedStatus,
        date: localDate,
        comments: comments
    };

    jQuery.ajax({
        type: "POST",
        url: 'update.php',
        dataType: 'json',
        data: {functionname: 'add', arguments: [lead_id, formDatap['status']]},
        success: function (obj, textstatus) {
                      if( !('error' in obj) ) {
                          yourVariable = obj.result;
                      }
                      else {
                          console.log(obj.error);
                      }
                }
    })};
    alert('Стадия успешно изменена')
}
