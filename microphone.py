import speech_recognition as sr
from fuzzywuzzy import fuzz


class Microphone:

    def __init__(self):
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
            r = sr.Recognizer()
            m = sr.Microphone(device_index=microphone_index)

            with m as source:
                r.adjust_for_ambient_noise(source)
        else:
            print("Microphone not found")
