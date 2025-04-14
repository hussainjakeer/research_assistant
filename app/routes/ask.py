from flask import Blueprint, request, jsonify
from app.utils import ask_question

ask_bp = Blueprint("ask", __name__, url_prefix="/api")

@ask_bp.route("/ask", methods=["POST"])
def ask():
    try:
        session_id = request.form.get("session_id")
        question = request.form.get("question")

        if not session_id or not question:
            return jsonify({"error": "Missing session_id or question"}), 400

        response = ask_question(session_id, question)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
