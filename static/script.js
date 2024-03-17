function show() {
    element = document.querySelector('.other_div');
    element.style.visibility = 'visible';
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

    alert(data[status], data[date], data[comment], data[saleid])

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


function toDateInputValue(dateObject){
    const local = new Date(dateObject);
    local.setMinutes(dateObject.getMinutes() - dateObject.getTimezoneOffset());
    return local.toJSON().slice(0,10);
};

document.getElementById('date').value = toDateInputValue(new Date());


function toLocalISOString(date) {
    const localDate = new Date(date - date.getTimezoneOffset() * 60000);

    localDate.setSeconds(null);
    localDate.setMilliseconds(null);
    return localDate.toISOString().slice(0, -1);
};
  
document.getElementById("date").value = toLocalISOString(new Date());


alert(toLocalISOString(new Date()))
