import pyttsx3
from threading import Thread


class SpeakEngine:

    def __init__(self, finished_utterance_callback):
        self.__pyttsx3 = pyttsx3.init()
        self.__pyttsx3.connect('finished-utterance', self.on_finished_utterance)
        self.__voices = self.__pyttsx3.getProperty("voices")
        self.__selected_voice = None
        self.__finished_utterance_callback = finished_utterance_callback

    def get_voices(self, language="ru_RU"):
        """Только если у вас установлены голоса для синтеза речи!"""
        result = []

        for voice in self.__voices:
            if language in voice.languages:
                print("Russian voice found: " + voice.name)
                result.append(voice)

        if len(result) == 0:
            print("No voices found for language {0}".format(language))

        return result

    def set_voice(self, voice):
        self.__selected_voice = voice
        self.__pyttsx3.setProperty('voice', voice.id)

    def speak(self, what):
        thread = Thread(target=self.__speak, args=(what,))
        thread.start()

    def __speak(self, what):
        print(what)
        self.__pyttsx3.say(what)
        self.__pyttsx3.startLoop()

    def on_finished_utterance(self, name, completed):
        print("on_finished_utterance")
        self.__finished_utterance_callback()
