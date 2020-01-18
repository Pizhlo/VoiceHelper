import tkinter as tk


class VoicesList(tk.Frame):

    def __init__(self, voices, voice_select_callback):
        super(VoicesList, self).__init__()
        self.voices = voices
        self.voice_select_callback = voice_select_callback
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Голосовые помощники")
        self.title_label.pack(side=tk.TOP)

        self.voices_listbox = tk.Listbox(self)
        self.voices_listbox.pack(side=tk.TOP, expand=1)
        self.voices_listbox.bind("<<ListboxSelect>>", self.voices_list_did_select_voice)

        for voice in self.voices:
            self.voices_listbox.insert(tk.END, voice.name)

    def voices_list_did_select_voice(self, event):
        """https://stackoverflow.com/a/12936031/3004003"""
        w = event.widget
        index = w.curselection()[0]
        self.voice_select_callback(self.voices[index])

