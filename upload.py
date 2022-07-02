from flask import *
from vnpd import detect_number_plate
import cv2

app = Flask(__name__)


@app.route("/")
def upload():
    return render_template("file_upload_form.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        f = request.files["file"]
        f.save(f.filename)
        if f.filename=='':
            return ('/')
        text = detect_number_plate(cv2.imread(f.filename))
        return render_template("success.html", name=f.filename, text=text)


if __name__ == "__main__":
    app.run(debug=True)
