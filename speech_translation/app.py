import logging

from service.service_app import SpeechApp


def create_app():
    """
    This is the factory method for flask. It is automatically detected when flask is run, but we must tell flask
    what python file to use:

        export FLASK_APP=app.py
        export FLASK_ENV=development
        flask run --host=0.0.0.0 --port=8888
    """
    logging.basicConfig(level=logging.DEBUG)

    # create and configure the app
    app = SpeechApp('speech_app')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
