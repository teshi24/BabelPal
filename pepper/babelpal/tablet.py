from cgitb import enable


class Tablet:
    robot = None
    tablet_service = None

    from_language = None
    to_language = None
    enabled = True

    def __init__(self, robot):
        self.robot = robot

        # display selection
        self.tablet_service = robot.session.service("ALTabletService")
        self.tablet_service.showImage("http://198.18.0.1/apps/babelpal_images/language_selection.png")
        self.tablet_service.onTouchUp.connect(self.onTouch)

    def stop_onTouch(self):
        self.enabled = False

    def start_onTouch(self):
        self.enabled = True

    def onTouch(self, x, y):
        if self.enabled:
            if self.from_language is None:
                language = self.getSelectedLanguage(x, y)
                if language is not None:
                    self.from_language = language
                    self.robot.ALTextToSpeech.say("First Language is "+ self.from_language)
            elif self.to_language is None:
                language = self.getSelectedLanguage(x, y)
                if language is not None:
                    self.to_language = language
                    self.robot.ALTextToSpeech.say("Second Language is " + self.to_language)
                    self.tablet_service.showImage("http://198.18.0.1/apps/babelpal_images/"+ self.from_language + "_" + self.to_language +".png")
            else:
                if 500 < x < 750 and 50 < y < 300:
                    self.switch_languages()
                elif 1100 < x < 1250 and 50 < y < 200:
                    self.back_to_main()
                else:
                    return None

    def switch_languages(self):
        temp = self.from_language
        self.from_language = self.to_language
        self.to_language = temp
        self.tablet_service.showImage("http://198.18.0.1/apps/babelpal_images/" + self.from_language + "_" + self.to_language + ".png")

    def back_to_main(self):
        self.from_language = None
        self.to_language = None
        self.tablet_service.showImage("http://198.18.0.1/apps/babelpal_images/language_selection.png")

    @staticmethod
    def getSelectedLanguage(x, y):
        if 150 < x < 500 and 150 < y < 450:
            return "spanish"
        elif 150 < x < 500 and 450 < y < 750:
            return "english"
        elif 750 < x < 1100 and 150 < y < 450:
            return "french"
        elif 750 < x < 1100 and 450 < y < 750:
            return "german"
        else:
            return None
