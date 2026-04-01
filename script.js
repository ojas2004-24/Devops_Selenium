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
        message.innerText = "Name cannot be empty";
        return false;
    }

    // Email validation
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        message.innerText = "Enter a valid email address";
        return false;
    }

    // Mobile validation
    let mobilePattern = /^[0-9]{10}$/;
    if (!mobilePattern.test(mobile)) {
        message.innerText = "Enter a valid 10-digit mobile number";
        return false;
    }

    // Department validation
    if (department === "") {
        message.innerText = "Please select a department";
        return false;
    }

    // Gender validation
    if (!gender) {
        message.innerText = "Please select gender";
        return false;
    }

    // Comments validation
    let words = comments.split(/\s+/).filter(word => word.length > 0);
    if (words.length < 10) {
        message.innerText = "Feedback must contain at least 10 words";
        return false;
    }

    // SUCCESS (no emoji 🚫)
    message.style.color = "green";
    message.innerText = "Form submitted successfully!";

    return false; // 🚀 IMPORTANT (prevent reload for Selenium)
}