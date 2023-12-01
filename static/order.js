document.getElementById("heading").remove()
let len = document.querySelectorAll("#remove").length
for (let i = 0; i < len; i++) {
    document.querySelector("#remove").remove()
}
document.getElementById("plcorder").remove()


// Payment Function
function initializePayment(orderId, amount) {
  let price = 50;
  if (num > 0) {
    for (let i = 0; i < localStorage.length; i++) {
      if (Number(localStorage.key(i))) {
        let id = localStorage.key(i);
        price +=JSON.parse(localStorage.getItem(id)).price *JSON.parse(localStorage.getItem(id)).quantity;
      }
    }
  }
  var options = {
    key: "rzp_test_lCl3lgTUtrCbDN",
    amount: price * 100,
    currency: "INR",
    name: "MADSHIP",
    description: "Product Purchase",
    order_id: orderId,
    handler: function (response) {
      // Handle the payment success or failure here
      if (response.razorpay_payment_id) {
        alert(
          "Payment successful! Payment ID: " + response.razorpay_payment_id
        );
      } else {
        alert("Payment failed");
      }
    },
  };

  var rzp1 = new Razorpay(options);
  rzp1.open();
}

// Direct Back Function
function forward() {
  window.history.back();
}
