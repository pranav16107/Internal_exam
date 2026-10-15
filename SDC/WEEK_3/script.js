// REGISTER VALIDATION

function register(event) {
  event.preventDefault();

  let name = document.getElementById("name").value.trim();
  let email = document.getElementById("email").value.trim();
  let password = document.getElementById("password").value;

  let valid = true;

  // Clear old errors

  document.getElementById("nameError").innerHTML = "";
  document.getElementById("emailError").innerHTML = "";
  document.getElementById("passwordError").innerHTML = "";

  // Name validation

  if (name == "") {
    document.getElementById("nameError").innerHTML = "Name is required";

    valid = false;
  }

  // Email validation

  let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  if (email == "") {
    document.getElementById("emailError").innerHTML = "Email is required";

    valid = false;
  } else if (!email.match(emailPattern)) {
    document.getElementById("emailError").innerHTML = "Enter a valid email";

    valid = false;
  }

  // Password validation

  if (password == "") {
    document.getElementById("passwordError").innerHTML = "Password is required";

    valid = false;
  } else if (password.length < 6) {
    document.getElementById("passwordError").innerHTML =
      "Password must contain at least 6 characters";

    valid = false;
  }

  // If everything is valid

  if (valid) {
    let user = {
      name: name,
      email: email,
      password: password,
    };

    localStorage.setItem("user", JSON.stringify(user));

    alert("Registration successful!");

    window.location.href = "login.html";
  }
}

// LOGIN VALIDATION

function login(event) {
  event.preventDefault();

  let email = document.getElementById("loginEmail").value.trim();

  let password = document.getElementById("loginPassword").value;

  let valid = true;

  // Clear old errors

  document.getElementById("loginEmailError").innerHTML = "";

  document.getElementById("loginPasswordError").innerHTML = "";

  // Email validation

  if (email == "") {
    document.getElementById("loginEmailError").innerHTML = "Email is required";

    valid = false;
  }

  // Password validation

  if (password == "") {
    document.getElementById("loginPasswordError").innerHTML =
      "Password is required";

    valid = false;
  }

  if (!valid) {
    return;
  }

  // Get registered user

  let user = JSON.parse(localStorage.getItem("user"));

  if (user == null) {
    alert("Please register first!");

    return;
  }

  // Check login details

  if (email == user.email && password == user.password) {
    alert("Login successful!");

    window.location.href = "index.html";
  } else {
    alert("Invalid email or password!");
  }
}

// CART

let cart = JSON.parse(localStorage.getItem("cart")) || [];

// ADD TO CART

function addCart(name, price) {
  cart.push({
    name: name,
    price: price,
  });

  localStorage.setItem("cart", JSON.stringify(cart));

  showCart();

  alert("Added to cart!");
}

// SHOW CART

function showCart() {
  let cartDiv = document.getElementById("cart");
  let total = document.getElementById("total");

  if (cartDiv == null) {
    return;
  }

  if (cart.length == 0) {
    cartDiv.innerHTML = "Cart is empty";

    total.innerHTML = "0";

    return;
  }

  let output = "";
  let sum = 0;

  for (let i = 0; i < cart.length; i++) {
    output += `
            <div class="border p-2 mt-2">

                ${cart[i].name} - ₹${cart[i].price}

                <button class="btn btn-danger btn-sm float-end"
                        onclick="removeCart(${i})">
                    Remove
                </button>

            </div>
        `;

    sum += cart[i].price;
  }

  cartDiv.innerHTML = output;

  total.innerHTML = sum;
}

// REMOVE CART ITEM

function removeCart(index) {
  cart.splice(index, 1);

  localStorage.setItem("cart", JSON.stringify(cart));

  showCart();
}

// CHECKOUT

function checkout() {
  if (cart.length == 0) {
    alert("Cart is empty!");

    return;
  }

  alert("Order placed successfully!");

  cart = [];

  localStorage.setItem("cart", JSON.stringify(cart));

  showCart();
}

// DISPLAY CART

showCart();
