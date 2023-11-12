var button = document.getElementById("classButton");

button.addEventListener("click", sendData);

function sendData() {
    var dataToSend = {
        key1: "value1",
        key2: "value2",
        // Add more data as needed
    };

    // Send the data to the Flask backend using an AJAX POST request
    fetch("/api/endpoint", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(dataToSend),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the Flask backend
        console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}