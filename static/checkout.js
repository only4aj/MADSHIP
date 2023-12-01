// Forward Button of Browser disabled
if (num == 0) {
  window.history.back();
}

// Payment Function
function initializePayment(orderId, amount) {
  console.log('89098')
  let name = document.getElementById("cstmrname").value
  let email = document.getElementById("cstmremail").value
  let address = document.getElementById("cstmraddress").value
  let phone = document.getElementById("cstmrphone").value
  let state = document.getElementById("cstmrstate").value
  let city = document.getElementById("cstmrcity").value
  let pincode = document.getElementById("cstmrpincode").value
  if ((name && email && address && phone && state && city && pincode)) {
    let price = 50;
    // document.getElementById("rzp-button1").type = "button"
    price = 50;
    if (num > 0) {
      for (let i = 0; i < localStorage.length; i++) {
        if (Number(localStorage.key(i))) {
          let id = localStorage.key(i);
          price +=
            JSON.parse(localStorage.getItem(id)).price *
            JSON.parse(localStorage.getItem(id)).quantity;
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

    localStorage.clear()
  }else{
    alert("Please fill all the details")
  }

}

// Direct Back Function
function forward() {
  window.history.back();
}

