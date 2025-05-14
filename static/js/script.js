function showConfirmation(event) {
    alert("Brukeren er lagret!");
}


window.onload = function () {
    const params = new URLSearchParams(window.location.search);
    if (params.get("registrert") === "true") {
        alert("Timer er registrert!");
    }
};