function show() {
    element = document.querySelector('.other_div')
    element.style.visibility = 'visible';;
  }

function hide() {
element = document.querySelector('.other_div')
element.style.visibility = 'visible';;
}

function saveFormData() {
    // Get selected status value
    var selectedStatus = document.getElementById("statusSelect").value;

    // Get date/time and comments
    var localDate = document.getElementById("localdate").value;
    var comments = document.getElementById("name").value;

    var lead_id = document.location.search

    // Create a data object
    var formData = {
        status: selectedStatus,
        date: localDate,
        comments: comments
    };

    alert(lead_id)


    jQuery.ajax({
        type: "POST",
        url: 'your_functions_address.php',
        dataType: 'json',
        data: {functionname: 'add', arguments: [formData['status'], formData['date'], formData['comments']]},
    
        success: function (obj, textstatus) {
                      if( !('error' in obj) ) {
                          yourVariable = obj.result;
                      }
                      else {
                          console.log(obj.error);
                      }
                }
    });
}
