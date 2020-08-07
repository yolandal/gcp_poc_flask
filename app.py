from flask import Flask, request, jsonify
from datetime import datetime

import config

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to Bell-GCP POC"


@app.route("/msg", methods=["POST"])
def display_message():

    payload = request.get_json(force=True)

    output_payload = jsonify(
        ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        sentiment='Static',
        message=payload['message']
    )
    return output_payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
