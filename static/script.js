document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        // Basic form validation
        const transportType = document.getElementById("transport").value.trim();
        const distance = document.getElementById("distance").value;
        const energyUsage = document.getElementById("energy").value;
        const dietType = document.getElementById("diet").value.trim();

        if (!transportType || !distance || !energyUsage || !dietType) {
            event.preventDefault();
            alert("Please fill out all fields!");
        }
    });
});
