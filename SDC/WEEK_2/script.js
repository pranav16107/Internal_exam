// REGISTER

function register(event) {
  event.preventDefault();

  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;

  let user = {
    name: name,
    email: email,
    password: password,
  };

  localStorage.setItem("user", JSON.stringify(user));

  alert("Registration successful!");

  window.location.href = "login.html";
}

// LOGIN

function login(event) {
  event.preventDefault();

  let email = document.getElementById("loginEmail").value;
  let password = document.getElementById("loginPassword").value;

  let user = JSON.parse(localStorage.getItem("user"));

  if (user == null) {
    alert("Please register first!");

    return;
  }

  if (email == user.email && password == user.password) {
    alert("Login successful!");

    window.location.href = "index.html";
  } else {
    alert("Wrong email or password!");
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

// REMOVE FROM CART

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

// SHOW CART WHEN PAGE LOADS

showCart();
