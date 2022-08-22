alert("Open the chat");

var count = prompt(
  "amount to be spammed: ",
  "2"
);


if (!count || isNaN(count) || count < 0 || count > 1000) {
  alert();
} else {
  var message = prompt("write the msg: ", "hy");
  if (message == null || message == "") {
    alert();
  } else {
    console.clear();

    for (let i = 0; i < count; i++) {
      console.log(`"${message}" sent -> ${i + 1} times`);

      var box = document.querySelectorAll("[role=textbox]")[1];

      InputEvent = Event || InputEvent;
      var evt = new InputEvent("input", {
        bubbles: true,
        composer: true,
      });
      box.innerHTML = message;
      box.dispatchEvent(evt);

      box.parentElement.parentElement.parentElement.children[1].children[0].click();
    }
  }
}