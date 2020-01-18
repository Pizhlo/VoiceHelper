import tkinter as tk


class VoicesList(tk.Frame):

    def __init__(self, voices):
        super(VoicesList, self).__init__()
        self.voices = voices
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Голосовые помощники")
        self.title_label.pack(side=tk.TOP)

        self.voices_listbox = tk.Listbox(self)
        self.voices_listbox.pack(side=tk.TOP, expand=1)

        for voice in self.voices:
            self.voices_listbox.insert(tk.END, voice.name)
