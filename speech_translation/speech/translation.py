import os

from google.cloud import translate_v2 as translate


def translate_text(target: str, text: str) -> dict:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_secret_key.json'
    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-16")

    result = translate_client.translate(text, target_language=target, format_='text')

    return result
