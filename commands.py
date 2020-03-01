import tkinter as tk


class Menu(tk.Frame):

    def __init__(self, command_list):
        super(Menu, self).__init__()
        self.create_widgets(command_list)

    def create_widgets(self, commands):
        self.title_label = tk.Label(self, text="Меню")
        self.title_label.pack(side=tk.TOP)
        self.menu_listbox = tk.Listbox(self)
        self.menu_listbox.pack(side=tk.TOP)
        for element in commands:
            self.menu_listbox.insert(tk.END, element)
