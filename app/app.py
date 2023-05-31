import os
import pickle as pkl

from flask import Flask, request, jsonify, Response
from werkzeug.middleware.proxy_fix import ProxyFix

from inference.inference import model_fn, transform_fn


app = Flask(__name__)

model, preprocess_conf = model_fn(os.environ["SM_MODEL_DIR"])
encoders = preprocess_conf['encoders']
del preprocess_conf


@app.route("/ping", methods=["GET"])
def ping():
    if model is not None:
        return 'pong', 200
    else:
        return '', 500


@app.route("/invocations", methods=["POST"])
def invocations():
    content_type = request.headers['Content-Type']
    if content_type == 'text/csv':
        data = request.data.decode('utf-8')
        preds = {
            'Attrition': transform_fn(model, data, content_type, encoders)
        }
        return jsonify(preds)
    else:
        return 'Unsupported Media Type', 415
