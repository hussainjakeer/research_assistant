from flask import Blueprint, request, jsonify
from app.utils import save_pdf, process_and_store_pdf
import os

upload_bp = Blueprint("upload", __name__, url_prefix="/api")

@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    try:
        session_id = request.form.get("session_id")
        file = request.files["file"]
        if not file or not session_id:
            return jsonify({"error": "Missing file or session ID"}), 400

        file_path = save_pdf(file, file.filename)
        process_and_store_pdf(session_id, file_path)
        os.remove(file_path)

        return jsonify({"message": "File processed successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
