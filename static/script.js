function show() {
    element = document.querySelector('.other_div')
    element.style.visibility = 'visible';;
  }

  function submitForm() {
    var selectedSaleId = window.location.pathname;
    var selectedStatus = document.getElementById("statusSelect").value;
    var selectedDate = document.getElementById('date').value;
    var selectedComment = document.getElementById('comment').value;

    var data = {
        status: selectedStatus,
        date: selectedDate,
        comment: selectedComment,
        saleid: selectedSaleId
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
    alert(selectedStatus)
    alert('Данные отправлены в CRM')
}
