#
# Пользовательский интерфейс настройки
#

import tkinter as tk
import dop
from voices_list import VoicesList

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        buttons_width = '25'
        buttons_height = '10'

        self.button_change_voice = tk.Button(self, text="Изменить голос",
                                             width=buttons_width, height=buttons_height)
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

        self.voices_list = VoicesList(dop.ru_voices)
        self.voices_list.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)

# Окно

def main():
    root = tk.Tk()
    root.title("Настройка голосового помощника")
    root.geometry('1020x620')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
