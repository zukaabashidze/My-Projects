let count = 172;
setInterval(() => {
    count += Math.floor(Math.random() * 5 - 2); // რანდომი მატება/კლება
    document.getElementById("car-text").textContent = count;
}, 3000);