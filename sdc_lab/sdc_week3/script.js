let items = [];
let total = 0;

function show(id) {
    document.querySelectorAll(".page").forEach(p => p.style.display = "none");
    document.getElementById(id).style.display = "block";
}

function add(price) {
    items.push(price);
    total += price;
    update();
}

function removeItem(i) {
    total -= items[i];
    items.splice(i, 1);
    update();
}

function update() {
    document.getElementById("cart").innerHTML = items.map((p, i) =>
        "Product " + (p == 100 ? "1" : "2") + " - Rs. " + p +
        ' <button class="btn btn-secondary btn-sm" onclick="removeItem(' + i + ')">Remove</button>'
    ).join("<br>") || "Cart is empty";

    document.getElementById("total").innerHTML = "Total: Rs. " + total;
}

function order() {
    if (items.length == 0) {
        alert("Cart is empty!");
    } else {
        alert("Order placed successfully!");
        items = [];
        total = 0;
        update();
    }
}

function validateLogin() {
    let u = document.getElementById("username").value.trim();
    let p = document.getElementById("loginPassword").value;

    if (u == "" || p == "") {
        alert("Please fill all fields");
    } else if (p.length < 6) {
        alert("Password must contain at least 6 characters");
    } else {
        alert("Login validation successful");
    }

    return false;
}

function validateRegister() {
    let n = document.getElementById("name").value.trim();
    let e = document.getElementById("email").value.trim();
    let p = document.getElementById("password").value;
    let c = document.getElementById("confirmPassword").value;

    if (n == "" || e == "" || p == "" || c == "") {
        alert("Please fill all fields");
    } else if (!e.includes("@") || !e.includes(".")) {
        alert("Enter a valid email");
    } else if (p.length < 6) {
        alert("Password must contain at least 6 characters");
    } else if (p != c) {
        alert("Passwords do not match");
    } else {
        alert("Registration validation successful");
    }

    return false;
}

show("home");
update();