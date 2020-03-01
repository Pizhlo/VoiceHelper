import datetime
import speech_recognition as sr
from fuzzywuzzy import fuzz
from recognizer_commands import RecognizerCommands



class Recognizer:

    def __init__(self, speak_engine):
        self.recognition_is_running = False
        self.__speak_engine = speak_engine
        self.__init_recognition()

    def __init_recognition(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Device with name \"{1}\" index {0}".format(index, name))

        microphone_index = -1
        audio = sr.Microphone.get_pyaudio().PyAudio()

        for i in range(audio.get_device_count()):
            device_info = audio.get_device_info_by_index(i)

            if device_info.get("maxInputChannels") > 0:
                microphone_index = i
                break

        if microphone_index >= 0:
            self.__recognizer = sr.Recognizer()
            self.__microphone = sr.Microphone(device_index=microphone_index)

            with self.__microphone as source:
                self.__recognizer.adjust_for_ambient_noise(source)

            self.__commands = RecognizerCommands.default_commands
        else:
            print("Microphone not found")

    def __recognize_cmd(self, cmd):
        result = {'cmd': '', 'percent': 0}

        for c, v in self.__commands['cmds'].items():
            for x in v:
                ratio = fuzz.ratio(cmd, x)

                if ratio > result['percent']:
                    result['cmd'] = c
                    result['percent'] = ratio

        return result

    def __execute_cmd(self, cmd):
        if cmd == 'ctime':
            # сказать текущее время
            now = datetime.datetime.now()
            self.__speak_engine.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

        elif cmd == 'stupid1':
            # рассказать анекдот
            self.__speak_engine.speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

        else:
            print('Команда не распознана, повторите!')

    def __process_cmd(self, cmd):
        cmd = self.__recognize_cmd(cmd)
        self.__execute_cmd(cmd['cmd'])

    def start_recognition(self):
        self.recognition_is_running = True
        self.RecognizerCallback.command_callback = self.__process_cmd
        self.__stop_handler = self.__recognizer.listen_in_background(self.__microphone,
                                                                     self.RecognizerCallback.recognizer_callback)

    def stop_recognition(self):
        self.recognition_is_running = False

        try:
            self.__stop_handler()
        except AttributeError:
            pass

    class RecognizerCallback:
        command_callback = None

        @staticmethod
        def recognizer_callback(recognizer, audio):
            try:
                voice = recognizer.recognize_google(audio, language="ru-RU").lower()
                commands = RecognizerCommands.default_commands
                print("Распознано: " + voice)

                # if voice.startswith(commands["alias"]):
                # обращаются к Компьютеру
                cmd = voice

                for x in commands['alias']:
                    cmd = cmd.replace(x, "").strip()

                for x in commands['tbr']:
                    cmd = cmd.replace(x, "").strip()

                Recognizer.RecognizerCallback.command_callback(cmd)

            except sr.UnknownValueError:
                print("Голос не распознан!")
            except sr.RequestError as e:
                print("Неизвестная ошибка, проверьте интернет!".format(e))
            except AttributeError as e:
                print(e)
