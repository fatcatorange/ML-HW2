document.addEventListener('DOMContentLoaded', function() {
    let button = document.getElementById('submit');
    let chatBoard = document.getElementById('chatBoard');
    let input = document.getElementById('input');
    let chatContent = [];

    button.addEventListener('click', function() {
        chatContent.push(input.value);
        let container = document.createElement('div');
        container.className = "chat-container";
        let newDiv = document.createElement('div');
        newDiv.innerText = input.value;
        newDiv.className = "user-chat";
        input.value = "";
        container.appendChild(newDiv);
        chatBoard.appendChild(container);

        const url = 'http://127.0.0.1:8000/generate_response/';
        const data = { prompt: newDiv.innerText };
        const headers = { 'Content-Type': 'application/json' };

        // 使用 Fetch API 發送 POST 請求
        fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let container = document.createElement('div');
            container.className = "chat-container";
            let newDiv = document.createElement('div');
            newDiv.className = "res-chat";
            newDiv.innerText = data.data.response;
            chatBoard.appendChild(container);
            container.appendChild(newDiv);
        })
        .catch(error => {
            console.error('Error:', error);
        });

    })
});