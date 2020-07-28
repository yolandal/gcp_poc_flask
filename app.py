from flask import Flask, request
import json
import config

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Bell-GCP POC! The app has two end points: '/lob?lob=HP' and '/num?num=1'"


@app.route("/lob", methods=['GET','POST'])
def lob_to_num():
    d = {
        "HP": "1",
        "Mob": "2",
        "Int": "4",
        "TV": "5"
    }
    r = request.args.get('lob')

    if r not in ['HP','Mob','Int','TV']:
        raise ValueError("Use one of the following numbers: ['HP','Mob','Int','TV']")
    else:
        result = d[str(r)]

    return result


@app.route("/num")
def num_to_int():
    d = {
        "1": "HP",
        "2": "Mob",
        "4": "Int",
        "5": "TV"
    }
    r = request.args.get('num')

    if r not in ['1','2','4','5']:
        raise ValueError("Use one of the following numbers: [1,2,4,5]")
    else:
        result = d[str(r)]

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
