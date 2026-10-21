 // 1. Arrow function
const square = n => n * n;
document.write("Square: " + square(5) + "<br>");

// 2. Callback function
function display(callback) {
    callback();
}

display(() => {
    document.write("Callback executed<br>");
});

// 3. Promise with async/await
function message() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Promise resolved after 2 seconds");
        }, 2000);
    });
}

async function showMessage() {
    let result = await message();
    document.write(result);
}

showMessage();
