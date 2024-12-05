from babelpal.listen_on_head_touch import ListenOnHeadTouch
from babelpal.translation import TranslationFactory
from robot import PepperConfiguration, Robot

config = PepperConfiguration("Pale")
pepper = Robot(config)
translator = TranslationFactory.get_translation_service()

# todo: figure out where this fits
def say_translation():
    print("Stopped listening!")
    text = translator.translate()
    pepper.ALTextToSpeech.say(text)

ListenOnHeadTouch(pepper, translator.listen, say_translation)
pepper.app.run()
