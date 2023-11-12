document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.querySelector('.submitClasses');
  
    submitButton.addEventListener('click', function() {
      const inputs = document.querySelectorAll('.grid-item input');
      const data = Array.from(inputs).map(input => input.value);
  
      // Send the data to your Flask backend using fetch
      fetch('/submit_classes', { // The URL to your Flask route
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ classes: data }) // Convert your data to JSON
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    });
  });
  