import tkinter as tk
from voices_list import VoicesList
from speak_engine import SpeakEngine
from recognizer import Recognizer


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.speak_engine = SpeakEngine(self.speak_engine_did_finish_utterance)
        self.voices = self.speak_engine.get_voices()

        self.recognizer = Recognizer(self.speak_engine)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        buttons_width = '25'
        buttons_height = '10'

        self.button_change_voice = tk.Button(self, text="Изменить голос",
                                             width=buttons_width, height=buttons_height,
                                             command=self.button_change_voice_click)
        self.button_change_voice.pack(side=tk.LEFT)

        self.button_add_profile = tk.Button(self, text="Добавить профиль",
                                            width=buttons_width, height=buttons_height)
        self.button_add_profile.pack(side=tk.LEFT)

        self.button_make_new_command = tk.Button(self, text="Добавить команду",
                                                 width=buttons_width, height=buttons_height)
        self.button_make_new_command.pack(side=tk.LEFT)

        self.button_quit = tk.Button(self, text="Выйти из настроек",
                                     width=buttons_width, height=buttons_height,
                                     command=self.master.destroy)  # TODO: change command
        self.button_quit.pack(side=tk.LEFT)

        self.voices_list = VoicesList(self.voices, self.voices_list_did_select_voice)
        self.voices_list.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)

    def voices_list_did_select_voice(self, voice):
        print("Voice selected: {0}".format(voice.name))
        self.voices_list.state = tk.DISABLED

        self.speak_engine.set_voice(voice)
        self.speak_engine.speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

    def speak_engine_did_finish_utterance(self):
        print("utterance finished")
        self.voices_list.state = tk.NORMAL

    def button_change_voice_click(self):
        if not self.recognizer.recognition_is_running:
            self.recognizer.start_recognition()
        else:
            self.recognizer.stop_recognition()


def main():
    root = tk.Tk()
    root.title("Настройка голосового помощника")
    root.geometry('1020x620')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
