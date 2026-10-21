
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
        "Product " + (p === 100 ? "1" : "2") + " - Rs. " + p +
        ' <button class="btn btn-secondary btn-sm" onclick="removeItem(' + i + ')">Remove</button>'
    ).join("<br>") || "Cart is empty";

    document.getElementById("total").innerHTML = "Total: Rs. " + total;
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
update();
