import pandas as pd
from flask import Flask, request
from jsonschema import ValidationError
from loguru import logger

from validate import validate_features

app = Flask(__name__)


MODEL = None


@app.route("/predict", methods=["POST"])
def predict():
    global MODEL
    input = request.get_json(force=True)
    logger.info(f"Predict on {input}")
    try:
        validate_features(input)
        result = MODEL.predict(pd.DataFrame([input]))[0]
        input["result"] = result
        logger.info(f"EXHAUST: {input}")
        return result
    except ValidationError as e:
        msg = f"Bad Features: {str(e)}"
        logger.exception(msg)
        return msg

    return "Idk what happened but something went wrong."


def serve(model):
    global MODEL
    MODEL = model
    app.run(host="0.0.0.0")
