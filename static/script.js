function show() {
    element = document.querySelector('.other_div')
    element.style.visibility = 'visible';;
  }

  function submitForm() {
    var selectedSaleId = window.location.pathname.split('/');
    try {
        var selectedDate = document.getElementById('date').value;
    } catch (err) {
        selectedDate = None
    }
    var selectedStatus = document.getElementById("statusSelect").value;
    try {
        var selectedComment = document.getElementById('comment').value;
    } catch (err) {
        selectedComment = None
    }
    

    var data = {
        status: selectedStatus,
        date: selectedDate,
        comment: selectedComment,
        saleid: selectedSaleId[3]
    };

    alert(data)

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
        alert('Ошибка:', error);
    });
    alert('Данные отправлены в CRM')
}
