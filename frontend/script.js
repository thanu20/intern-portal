document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/api/user")
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("referral-code").textContent = data.referral_code;
      document.getElementById("total-donations").textContent = "₹" + data.total_donations;
    })
    .catch((err) => console.error("Error:", err));
});
