alert("Please make sure you have opened the chat you want to spam.");

var count = prompt(
  "Enter number of messages: \nPlease Enter a number between 0 and 100",
  "10"
);


if (!count || isNaN(count) || count < 0 || count > 1000) {
  alert(
    "Please enter a NUMBER between 0 and 100. \nYou can re-run the script now."
  );
} else {
  // Get the message to spam
  var message = prompt("MESSAGE YOU WANT TO SPAM : ", "Hello from spammer...");
  //make sure the user entered a message and it is not empty
  if (message == null || message == "") {
    alert("Please enter a message to spam. \nYou can re-run the script now.");
  } else {
    // Clear the current console for better visibility
    console.clear();

    // spam the messages
    for (let i = 0; i < count; i++) {
      console.log(`"${message}" sent -> ${i + 1} times`);

      // Get the input box
      var box = document.querySelectorAll("[id=message-input]")[1];

      // create event of type 'input' so that the whatsapp UI will update to sending text message instead of voice message
      InputEvent = Event || InputEvent;
      var evt = new InputEvent("input", {
        bubbles: true,
        composer: true,
      });
      box.innerHTML = message; // set the message as input box value
      box.dispatchEvent(evt); // trigger the event

      // This is bit of stratch to select the send button and click it
      // You need to climb up the DOM tree three levels and then to second child and then the first child is the send button
      box.parentElement.parentElement.parentElement.children[1].children[0].click();
    }
  }
}