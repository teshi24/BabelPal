import os
import sys

from google.cloud import speech

from constants import RATE, CHUNK, LANGUAGE_CODE
from speech.microphone_stream import MicrophoneStream


class SpeechToText:
    stream = None
    transcript = ''
    transcribing = True

    def start(self, language):
        self.transcript = ''
        self.transcribing = True

        language_code = LANGUAGE_CODE.get(language)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_secret_key.json'
        client = speech.SpeechClient()
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code
        )

        streaming_config = speech.StreamingRecognitionConfig(config=config)

        with MicrophoneStream(RATE, CHUNK) as stream:
            self.stream = stream
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )
            responses = client.streaming_recognize(streaming_config, requests)

            self.listen_print_loop(responses)

    def listen_print_loop(self, responses: object):

        num_chars_printed = 0
        for response in responses:
            if not response.results:
                continue

            result = response.results[0]
            if not result.alternatives:
                continue

            self.transcript = result.alternatives[0].transcript

            overwrite_chars = " " * (num_chars_printed - len(self.transcript))

            if not result.is_final:
                sys.stdout.write(self.transcript + overwrite_chars + "\r")
                sys.stdout.flush()
                num_chars_printed = len(self.transcript)

            else:
                print(self.transcript + overwrite_chars)
                num_chars_printed = 0
                self.transcribing = False

    def stop(self) -> str:
        self.stream.__exit__(None, None, None)
        return self.transcript
