function show() {
    element = document.querySelector('.other_div');
    element.style.visibility = 'visible';
  }

  function submitForm() {
    var selectedDate = null
    var selectedComment = null
    
    var selectedSaleId = window.location.pathname.split('/');
    var selectedStatus = document.getElementById("statusSelect").value;
    var selectedDate = document.getElementById('date').value;
    var selectedComment = document.getElementById('comment').value;
    

    var data = {
        status: selectedStatus,
        date: selectedDate,
        comment: selectedComment,
        saleid: selectedSaleId[3]
    };

    fetch('/process_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    })
    .catch(error => {
        alert(error);
    });
    alert('Данные отправлены в CRM')
}


