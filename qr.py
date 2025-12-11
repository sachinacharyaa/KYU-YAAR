from flask import Flask, request, jsonify
import qrcode
import base64
from io import BytesIO
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.post("/makeqr")
def makeqr():
    data = request.json["url"]
    # filename = request.json["filename"]

    qr = qrcode.QRCode(box_size=10, border=5)
    qr.add_data(data)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return jsonify({
        "qr": qr_base64
        #, "filename": filename + ".jpg"
    })

app.run(debug=True)
