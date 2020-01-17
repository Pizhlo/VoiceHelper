#
# Пользовательский интерфейс настройки
#

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        buttons_width = '25'
        buttons_height = '10'
        wrap_length = str(int(buttons_width) * 1)

        self.button_change_voice = tk.Button(self, text="Изменить голос \newef2wb  232323   23232323",
                                             width=buttons_width, height=buttons_height)
        self.button_change_voice.pack(side=tk.LEFT)

        self.button_quit = tk.Button(self, text="Добавить профиль",
                                     width=buttons_width, height=buttons_height)
        self.button_quit.pack(side=tk.LEFT)

        self.button_make_new_command = tk.Button(self, text="Добавить команду",
                                                 width=buttons_width, height=buttons_height)
        self.button_make_new_command.pack(side=tk.LEFT)

        self.button_quit = tk.Button(self, text="Выйти из настроек",
                                     width=buttons_width, height=buttons_height,
                                     command=self.master.destroy)  # TODO: change command
        self.button_quit.pack(side=tk.LEFT)


# Окно

def main():
    root = tk.Tk()
    root.title("Настройка голосового помощника")
    root.geometry('1020x620')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
