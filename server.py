# PDF Tools server: site bhi dikhata hai aur PDF to Word (asli layout) bhi karta hai.
import os, tempfile
from flask import Flask, request, send_file, send_from_directory, jsonify
from flask_cors import CORS
from pdf2docx import Converter

HERE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
CORS(app)
app.config["MAX_CONTENT_LENGTH"] = 30 * 1024 * 1024  # 30 MB

@app.get("/")
def home():
    return send_from_directory(HERE, "index.html")

@app.get("/health")
def health():
    return jsonify(ok=True, converter=True)

@app.post("/convert")
def convert():
    f = request.files.get("file")
    if not f:
        return jsonify(error="file missing"), 400
    d = tempfile.mkdtemp()
    src, out = os.path.join(d, "in.pdf"), os.path.join(d, "out.docx")
    f.save(src)
    cv = Converter(src)
    try:
        cv.convert(out)
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        cv.close()
    return send_file(out, as_attachment=True, download_name="converted.docx")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
