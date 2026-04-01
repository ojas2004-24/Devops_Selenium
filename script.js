function validateForm() {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let department = document.getElementById("department").value;
    let comments = document.getElementById("comments").value.trim();
    let gender = document.querySelector('input[name="gender"]:checked');
    let message = document.getElementById("message");

    message.style.color = "red";

    // Name validation
    if (name === "") {
        message.innerHTML = "⚠ Name cannot be empty";
        return;
    }

    // Email validation
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        message.innerHTML = "⚠ Enter a valid email address";
        return;
    }

    // Mobile validation
    let mobilePattern = /^[0-9]{10}$/;
    if (!mobilePattern.test(mobile)) {
        message.innerHTML = "⚠ Enter a valid 10-digit mobile number";
        return;
    }

    // Department validation
    if (department === "") {
        message.innerHTML = "⚠ Please select a department";
        return;
    }

    // Gender validation
    if (!gender) {
        message.innerHTML = "⚠ Please select gender";
        return;
    }

    // Comments validation (min 10 words)
    let words = comments.split(/\s+/).filter(word => word.length > 0);
    if (words.length < 10) {
        message.innerHTML = "⚠ Feedback must contain at least 10 words";
        return;
    }

    // Success
    message.style.color = "#00ffcc";
    message.innerHTML = "✅ Form submitted successfully!";
}