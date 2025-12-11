let btn = document.querySelector("#btn");

const QRGenerator = async () => {
    // Get values inside the function to capture latest input values on click
    let url = document.querySelector("#url").value;
    // let filename = document.querySelector("#filename").value;

    let response = await fetch("http://127.0.0.1:5000/makeqr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url, }),
        //  add bove filename: filename 
    });

    let data = await response.json();
    document.getElementById("qrImg").src = "data:image/jpeg;base64," + data.qr;
}

btn.addEventListener("click", QRGenerator);








