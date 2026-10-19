
function validate()
{
    var email = document.getElementById("email").value;
    var pass = document.getElementById("pass").value;

    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    document.getElementById("e1").innerHTML = "";
    document.getElementById("e2").innerHTML = "";

    var valid = true;

    if (!pattern.test(email))
    {
        document.getElementById("e1").innerHTML = "Invalid email";
        valid = false;
    }

    if (pass.length < 8 || !/[0-9]/.test(pass))
    {
        document.getElementById("e2").innerHTML =
        "Password must have 8 characters and one digit";
        valid = false;
    }

    return valid;
}
