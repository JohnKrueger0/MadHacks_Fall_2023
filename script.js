// /*this is for a fact button and is tied to button. can delete if not useful*/
// var factList = [
//     "Cybercrime costs 3.5 billion of US businesses in 2019.", 
//     "26 smart object are located near every human on earth.", 
//     "As od 2021, more than 500 hours of video are uploaded to Youtube every minute.",
//     "25.9% of the internet is in English, 19.4% in Chinese, and 8% in Spanish.", 
//     "98-99% of people have the internet in Denmark, Iceland, the United Arab Emirates, Kuwait, and Qatar.",
//     "By 2014, google had indexed over 130 trillion web pages.",
//     "4.1 billion email users registered worldwide in 2020.",
//     "Youtube's copyright-checking software scans over 100 years of video every day.",
//     "The word internet comes from internetworking or inter-system networking.",
//     "It wasn't until 1992, when the US Congress passed the Scientific Advanced Technology Act that commerical interest were allowed online.",
//     "1 in 6 marriages today occur because the couple met online.",
//     "People spend on average of 2.8 hours a day browsing the web on smartphones.",
//     "There are more than 1.93 billion website online.",
//     "Around 7 million blog posts get published per day."
//   ];
  
//   //var for button
//   var button = document.getElementById("classButton");
  
//   //var for output
//   var fact = document.getElementById("fact");
  
//   //var for counter
//   var counter = 0;
  
//   //event listener
//   if (button){
//   button.addEventListener("click", display);
//   }
  
//   //function
//   function display(){
//     fact.innerHTML = factList[counter];
//     counter++;
//     if(counter == factList.length){
//       counter = 0;
//     }
//   }
//   var slideIndex = 0;
  
//   function moveSlides(n){
//       showSlides(slideIndex +=n);
//   }
  
//   function showSlides(n){
//       var slides = document.getElementsByClassName("slides");
//       var lastSlide = slides.length - 1;
//       if(n > lastSlide){
//           slideIndex = 0;
//       }
//       if(n < 0){
//           slideIndex = lastSlide;
//       }
//       for(var i = 0; i < slides.length; i++){
//           // slides[slideIndex].class += "active";
//           slides[i].style.display = "none";
//       }
//       slides[slideIndex].style.display = "block";
//   }
  
//   showSlides(slideIndex);
  
var button = document.getElementById("sendDataButton");

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
  