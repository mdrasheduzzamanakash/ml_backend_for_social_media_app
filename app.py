import flask
import pickle
from flask import request, jsonify

app = flask.Flask(__name__)


__model_emotion = None


def load_saved_artifacts():
    global __model
    global __model_emotion
    if __model_emotion is None:
        with open('emotion_prediction_model_23_12_21.pickle', 'rb') as emo_f:
            __model_emotion = pickle.load(emo_f)


@app.route('/', methods=['GET'])
def home():
    text = request.args['text']
    load_saved_artifacts()
    response = jsonify({
        'emotion': __model_emotion.predict([text])[0]
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


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