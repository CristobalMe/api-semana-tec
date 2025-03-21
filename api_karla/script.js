
async function sendGet_encrypt() {
    const item_p = document.getElementById("p").value;
    if (!item_p) {
        alert("Please enter a prime number for p.");
        return;
    }

    const item_q = document.getElementById("q").value;
    if (!item_q) {
        alert("Please enter a prime number for q.");
        return;
    }

    const item_e = document.getElementById("e").value;
    if (!item_e) {
        alert("Please enter the exponent e.");
        return;
    }

    const item_message = document.getElementById("message").value;
    if (!item_message) {
        alert("Please enter a message.");
        return;
    }

    const url = `/p/q/e/me/?p=${encodeURIComponent(item_p)}&q=${encodeURIComponent(item_q)}&e=${encodeURIComponent(item_e)}&me=${encodeURIComponent(item_message)}`;
    console.log("Request URL: ", url);  // Log the URL to verify it's correct

    try {
        const response = await fetch(url, {
            method: "GET", // Make a GET request
        });

        // Check if the request was successful
        if (!response.ok) {
            throw new Error("Failed to send GET request");
        }

        const data = await response.json();
        document.getElementById("response").innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error("Error details:", error);  // Log the error for more details
        alert("Error while sending GET request.");
    }
}

async function sendGet_encrypti() {
    const item_p = document.getElementById("p").value; // Get input value
    if (!item_p) {
        alert("Please enter an item before sending.");
        return;
    }

    const item_q = document.getElementById("q").value; // Get input value
    if (!item_q) {
        alert("Please enter an item before sending.");
        return;
    }

    const item_e = document.getElementById("e").value; // Get input value
    if (!item_e) {
        alert("Please enter an item before sending.");
        return;
    }

    const item_message = document.getElementById("message").value; // Get input value
    if (!item_message) {
        alert("Please enter an item before sending.");
        return;
    }

    try {
        const response = await fetch(`/p/q/e/me/?p=${encodeURIComponent(item_p)}&q=${encodeURIComponent(item_q)}&e=${encodeURIComponent(item_e)}&message=${encodeURIComponent(item_message)}`, {
            method: "GET", // Make a GET request
        });

        // Check if the request was successful
        if (!response.ok) {
            throw new Error("Failed to send GET request");
        }

        const data = await response.json();
        document.getElementById("response").innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error(error);
        alert("Error while sending GET request.");
    }
}
