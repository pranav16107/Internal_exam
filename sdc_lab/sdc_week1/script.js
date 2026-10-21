
let total = 0;
let items = [];

function show(id) {
    document.querySelectorAll(".page").forEach(function(p) {
        p.style.display = "none";
    });

    document.getElementById(id).style.display = "block";
}

function add(price) {
    items.push(price);
    total += price;
    update();
}

function update() {
    document.getElementById("cart").innerHTML =
        items.map(function(price, i) {
            return "Product " + (price === 100 ? "1" : "2") +
                " - Rs. " + price +
                ' <button onclick="remove(' + i + ')">Remove</button><br>';
        }).join("");

    if (items.length === 0) {
        document.getElementById("cart").innerHTML = "Cart is empty";
    }

    document.getElementById("total").innerHTML =
        "Total: Rs. " + total;
}

function remove(i) {
    total -= items[i];
    items.splice(i, 1);
    update();
}

function order() {
    if (items.length === 0) {
        alert("Cart is empty!");
    } else {
        alert("Order placed successfully!");
        items = [];
        total = 0;
        update();
    }
}

show("home");
