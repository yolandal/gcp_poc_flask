from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Bell-GCP POC! This is the home page of a Flask app."


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
