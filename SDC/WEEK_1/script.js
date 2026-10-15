let cart = [];
let total = 0;
// REGISTER
function register(event) {
    event.preventDefault();
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    localStorage.setItem("username", username);
    localStorage.setItem("email", email);
    localStorage.setItem("password", password);
    alert("Registration Successful!");
    window.location.href = "login.html";
}
// LOGIN
function login(event) {
    event.preventDefault();
    let email = document.getElementById("loginEmail").value;
    let password = document.getElementById("loginPassword").value;
    let savedEmail = localStorage.getItem("email");
    let savedPassword = localStorage.getItem("password");
    if (email == savedEmail && password == savedPassword) {
        alert("Login Successful!");
        window.location.href = "index.html";
    } else {
        alert("Invalid Email or Password!");
    }
}
// ADD TO CART
function addCart(name, price) {
    cart.push(name);
    total = total + price;
    document.getElementById("cartItems").innerHTML =
        cart.join("<br>");
    document.getElementById("total").innerHTML = total;
}
// CHECKOUT
function checkout() {
    alert("Thank you for shopping!");
    cart = [];
    total = 0;
    document.getElementById("cartItems").innerHTML = "";
    document.getElementById("total").innerHTML = 0;
}