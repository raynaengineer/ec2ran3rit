from flask import Flask, render_template, request, jsonify
from ai import chat, clear_memory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def handle_chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    response = chat(user_input)
    return jsonify({"response": response})


@app.route("/clear", methods=["POST"])
def clear_chat():
    clear_memory()
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=False)