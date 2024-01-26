function show() {
    element = document.querySelector('.other_div')
    element.style.visibility = 'visible';;
  }

function submitForm() {
    // Get selected status value
    var selectedStatus = document.getElementById("statusSelect").value;

    // Get date/time and comments
    var localDate = document.getElementById("localdate").value;
    var comments = document.getElementById("name").value;

    var lead_id = document.location.search
    var lead_id = lead_id.substring(1);

    // Create a data object
    var formData = {
        status: selectedStatus,
        date: localDate,
        comments: comments
    };
    };

    fetch('/process_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = result.result;
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
