#from pepper_robots import PepperConfiguration, Robot
from pepper.babelpal.listen_on_head_touch import ListenOnHeadTouch
from pepper.babelpal.translation import TranslationFactory
from pepper.pepper_robots import PepperConfiguration, Robot

config = PepperConfiguration("Pale")
pepper = Robot(config)
translator = TranslationFactory.get_translation_service(pepper)

# todo: figure out where this fits
def say_translation():
    print("Stopped listening!")
    text = translator.translate()
    pepper.ALTextToSpeech.say(text)

ListenOnHeadTouch(pepper, translator.listen, say_translation)
pepper.app.run()
