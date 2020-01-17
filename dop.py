# Голосовой ассистент Мой Комьютер
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
from configparser import ConfigParser

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Device with name \"{1}\" index {0}".format(index, name))

microphoneIndex = -1
audio = sr.Microphone.get_pyaudio().PyAudio()
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)

    if device_info.get("maxInputChannels") > 0:
        microphoneIndex = i
        break

if microphoneIndex < 0:
    print("Microphone not found")
    exit(1)

# настройки
opts = {
    "alias": ('Компьютер'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', "откройте", "скажите", "прекратите"),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты')
    }
}


# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Компьютеру
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

    else:
        print('Команда не распознана, повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=microphoneIndex)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!

voices = speak_engine.getProperty('voices')
ru_voices = []

for voice in voices:
    if voice.languages[0] == "ru_RU":
        print("RU voice found: " + voice.name)
        ru_voices.append(voice)

if len(ru_voices) == 0:
    print("No Russian voices found")
    exit(1)

speak_engine.setProperty('voice', ru_voices[0].id)

# forced cmd test
speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

# speak("Добрый день, повелитель")
# speak("Кеша слушает")

# stop_listening = r.listen_in_background(m, callback)
# while True: time.sleep(0.1) # infinity loop