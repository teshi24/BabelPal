import threading
import time
from http import HTTPStatus

from flask import jsonify, Blueprint

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
    listening = threading.Thread(target=speechToText.start)
    listening.start()
    return jsonify('Start Received'), HTTPStatus.OK


@app.route('/' + STOP_SPEECH, methods=['GET'])
def stop_speech():
    """
    Stops the stream

    Returns:
        - The recognized text in the language requested
    """
    while speechToText.transcribing is True:
        time.sleep(0.2)
    text_input = speechToText.stop()
    text_output = translate_text("en", text_input)
    return jsonify(text_output["translatedText"]), HTTPStatus.OK
