#
# Пользовательский интерфейс настройки
#
from tkinter import *

# Окно

root = Tk()
root.title("Настройка головосового пощоника")
root.geometry('1020x620')


# выход из программы


def quit():
    global root
    root.quit()


# изменить голос


button_changeVoice = Button(root, text="Изменить голос", width='25', height='10')
button_changeVoice.pack()
button_changeVoice.place(x=20, y=120)

# кнопка выхода

button_quit = Button(root, text="Выйти из настроек", width='25', height='10',
                     command=lambda root=root: quit())
button_quit.place(x=20, y=350)
button_quit.pack()

button_quit = Button(root, text="Добавить профиль", width='25', height='10')
button_quit.place(x=400, y=120)
button_quit.pack()

button_makeNewCommand = Button(root, text="Добавить команду", width='25', height='10')
button_makeNewCommand.place(x=400 , y=350)
button_makeNewCommand.pack()

root.mainloop()
