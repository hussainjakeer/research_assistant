from flask import Blueprint, request, jsonify
from app.utils import summarize_paper

summarize_bp = Blueprint("summarize", __name__, url_prefix="/api")

@summarize_bp.route("/summarize", methods=["POST"])
def summarize():
    try:
        session_id = request.form.get("session_id")
        if not session_id:
            return jsonify({"error": "Missing session_id"}), 400

        summary = summarize_paper(session_id)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
