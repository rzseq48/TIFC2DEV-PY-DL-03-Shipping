import os

from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")


@app.route("/")
def home():
    return jsonify({
        "message": "DL-03 Shipping What You Build is running!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/config-check")
def config_check():
    secret_key = app.config.get("JWT_SECRET_KEY")

    if not secret_key:
        raise RuntimeError("JWT_SECRET_KEY is not configured")

    return jsonify({
        "status": "ok",
        "message": "Environment variable is configured"
    })

if __name__ == "__main__":
    app.run(debug=True)