import threading
import time
from http import HTTPStatus

from flask import jsonify, Blueprint, request

from constants import LANGUAGE_CODE_TRANSLATION
from speech.speech_to_text import SpeechToText
from speech.translation import translate_text

PATH_PREFIX = '/'
START_SPEECH = '/start'
STOP_SPEECH = '/stop'

app = Blueprint(PATH_PREFIX, __name__)
speechToText: SpeechToText = SpeechToText()


@app.route('/' + START_SPEECH, methods=['GET'])
def start_speech():
    """
    Starts the stream to get text from the microphone
    """
    print("start sent")
    language = request.args.get('language')
    listening = threading.Thread(target=speechToText.start, args=(language,))
    listening.start()
    return jsonify('Start Received'), HTTPStatus.OK


@app.route('/' + STOP_SPEECH, methods=['GET'])
def stop_speech():
    """
    Stops the stream

    Returns:
        - The recognized text in the language requested
    """
    print("stop sent")
    language = request.args.get('language')
    language_code = LANGUAGE_CODE_TRANSLATION.get(language)
    while speechToText.transcribing is True:
        time.sleep(0.2)
    text_input = speechToText.stop()
    text_output = translate_text(language_code, text_input)
    return jsonify(text_output["translatedText"]), HTTPStatus.OK



@app.route('/test', methods=['GET'])
def test():

    return jsonify("test"), HTTPStatus.OK
