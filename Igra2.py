# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from random import choice
from tkinter import messagebox
from datetime import datetime

root = Tk()

root['bg'] = 'gray22'

def dismiss(window):
    window.grab_release()
    window.destroy()
    buttonExample.config(state='normal')

def update_time(): #Функция обновления настоящего времени
    label.config(text=f"{datetime.now():%H:%M:%S}")
    root.after(100, update_time)  # Запланировать выполнение этой же функции через 100 миллисекунд


def createNewWindow(): #Функция создания окна с правила игры
    print(x)
    newWindow = Toplevel(root)
    newWindow.attributes("-topmost", False)
    newWindow.title('Быки и коровы')
    newWindow.geometry('800x800')
    newWindow.resizable(False, False)
    newWindow['bg'] = 'gray22'
    newWindow.protocol("WM_DELETE_WINDOW", lambda: dismiss(newWindow))
    buttonExample.config(state='disabled')
    labelExample = tkinter.Label(newWindow, width=400, padx=10, pady=5, justify="center", text = 'Компьютер загадывает число. Цифры от 0 до 9 в числе не повторяются,\n при этом 0 может стоять на первом месте. В вводимом числе должно быть 4 цифры.\n Игрок вводит свой вариант числа, компьютер сравнивает его с\n "загаданным" числом и выдает результат в виде количества «Быков» и «Коров».\n Количество «Быков» - количество цифр которые присутствуют в\n загаданном числе и стоят на своем месте.\n Количество «Коров» - количество цифр присутствующих в загаданном\n числе, но стоящих не на своем месте.\n Игрок анализирует результат, и вводит следующий вариант.\n Соответственно после каждой такой попытки будут выводиться кол-во "Быков"\n и "Коров" ')
    labelExample.pack(anchor=N)
    labelExample.config(fg='white',
           font=('Courier', 13, 'italic'), bg='gray22')
    label2 = tkinter.Label(newWindow, width=400, padx=10, pady=5, justify="center", text='У вас будет ограничение в 15 ходов!')
    label2.pack(anchor=N)
    label2.config(fg='red',
            font=('Courier', 15, 'italic'), bg='gray22')
    close_button = tkinter.Button(newWindow, text="Закрыть правила",bg='grey', fg='red', font='Helvetica 12', command=lambda: dismiss(newWindow), pady=10, padx=10)
    close_button.place(x=330, y=600)
    can = Canvas(newWindow,bg='gray22', width=380, height=308, highlightthickness=2)
    can.place(x=205, y=270)
    can.create_image(0, 0, image=png4, anchor=NW)


window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
o = int((screen_width / 2) - (window_width / 2))
q = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, o, q))
label = tkinter.Label(root, font=("helvetica", 15), bg='gray22', fg='white')
label.pack()
root.iconbitmap('ishak.ico')
update_time()

x = ''
n = 0
k = 0
j = 0
p = ('~', '`', '!', '@', '#', '№', '$', '%', '^', '&', '?', '*', '(', ')', '_', '-', '+', '/', '>', '<', ':', ';', '"', ".", "|", "[","]","{","}","'","^",",", '\\')

def on_closing(): #Функция вывода окна с вопросом, и выход из приложения при положительном ответе
 if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
  root.destroy()

def play(event): #Основная игровая функция, привязанная к Entry
    global x, n, k, p, m
    m = 16
    if len(x) == 0: #Генерация числа
        z = '0123456789'
        x = choice(z[1:10])
        for i in range(3):
            z = ''.join(z.split(x[i]))
            x += choice(z)
            sms2.config(text='')
    y = Entry.get()
    print(x)
    can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can.place(x=0, y=50)
    can.create_image(0, 0, image=png3, anchor=NW)
    can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can2.place(x=0, y=200)
    can2.create_image(0, 0, image=png3, anchor=NW)
    can3 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can3.place(x=0, y=350)
    can3.create_image(0, 0, image=png3, anchor=NW)
    can4 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can4.place(x=0, y=500)
    can4.create_image(0, 0, image=png3, anchor=NW)
    can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)      #Все холсты после выполнения хода закрашиваются фоном приложения
    can5.place(x=615, y=50)
    can5.create_image(0, 0, image=png3, anchor=NW)
    can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can6.place(x=615, y=200)
    can6.create_image(0, 0, image=png3, anchor=NW)
    can7 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can7.place(x=615, y=350)
    can7.create_image(0, 0, image=png3, anchor=NW)
    can8 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
    can8.place(x=615, y=500)
    can8.create_image(0, 0, image=png3, anchor=NW)

    b = 0
    c = 0
    k = 0
    if y == '':  # Проверка на то пустое ли поле ввода
        messagebox.showerror("Исправьте", "Поле для ввода пусто")
        Entry.delete(0, END)
        return
    if len(y) > 4:  # Проверка на кол-во символом
        messagebox.showerror("Исправьте", "Введенное число содержит больше 4 символов")
        k = k + 1
        Entry.delete(0, END)
        return
    elif len(y) < 4:  # Проверка на кол-во символом
        messagebox.showerror('Исправьте', 'Введенное число содержит меньше 4 символов')
        k = k + 1
        Entry.delete(0, END)
    else:
        for i in range(len(y)): # Проверка на наличие пробелов
            if y[i-1] == ' ':
                messagebox.showerror("Исправьте", "Введенное число содержит ПРОБЕЛ")
                k = k+1
                Entry.delete(0, END)
                return
            elif (y[i] == y[(len(y) - i)-1] or y[2] == y[3] or y[1] == y[2] or y[0] == y[1] or y[1] == y[3] or y[0] == y[2]): # Проверка на уникальность
                messagebox.showerror("Исправьте", "Введенное число содержит одинаковые символы")
                k = k+1
                Entry.delete(0, END)
                return
            elif y[i] in p: #Проверка на спецсимволы
                messagebox.showerror('Исправьте', 'Введенное число содержит спецсимволы')
                k = k + 1
                Entry.delete(0, END)
                return
        if y.isalnum() == True: # Проверка на наличие букв
            if y.isnumeric() == False:
                messagebox.showerror("Исправьте", "Введенное число содержит БУКВЫ")
                k = k + 1
                Entry.delete(0, END)
    if k==0: #Проверка на кол-во "Быков" и "Коров"
        for i in range(4):
            if x[i] == y[i]:
                b += 1
            elif y[i] in x:
                c += 1
    if b == 1:
        can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can.place(x=0, y=50)
        can.create_image(0, 0, image=png, anchor=NW)
    if b == 2:
        can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can.place(x=0, y=50)
        can.create_image(0, 0, image=png, anchor=NW)
        can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can2.place(x=0, y=200)
        can2.create_image(0, 0, image=png, anchor=NW)
    if b == 3:
        can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can.place(x=0, y=50)
        can.create_image(0, 0, image=png, anchor=NW)
        can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can2.place(x=0, y=200)
        can2.create_image(0, 0, image=png, anchor=NW)
        can3 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can3.place(x=0, y=350)
        can3.create_image(0, 0, image=png, anchor=NW)
    if b == 4:
        can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can.place(x=0, y=50)
        can.create_image(0, 0, image=png, anchor=NW)
        can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can2.place(x=0, y=200)
        can2.create_image(0, 0, image=png, anchor=NW)
        can3 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can3.place(x=0, y=350)
        can3.create_image(0, 0, image=png, anchor=NW)
        can4 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can4.place(x=0, y=500)
        can4.create_image(0, 0, image=png, anchor=NW)
    if c == 1:
        can5 = Canvas(bg='gray22', width=185, height=183, highlightthickness=0)
        can5.place(x=615, y=50)
        can5.create_image(0, 0, image=png2, anchor=NW)
    if c == 2:
        can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can5.place(x=615, y=50)
        can5.create_image(0, 0, image=png2, anchor=NW)
        can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can6.place(x=615, y=200)
        can6.create_image(0, 0, image=png2, anchor=NW)
    if c == 3:
        can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can5.place(x=615, y=50)
        can5.create_image(0, 0, image=png2, anchor=NW)
        can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can6.place(x=615, y=200)
        can6.create_image(0, 0, image=png2, anchor=NW)
        can7 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can7.place(x=615, y=350)
        can7.create_image(0, 0, image=png2, anchor=NW)
    if c == 4:
        can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can5.place(x=615, y=50)
        can5.create_image(0, 0, image=png2, anchor=NW)
        can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can6.place(x=615, y=200)
        can6.create_image(0, 0, image=png2, anchor=NW)
        can7 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can7.place(x=615, y=350)
        can7.create_image(0, 0, image=png2, anchor=NW)
        can8 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can8.place(x=615, y=500)
        can8.create_image(0, 0, image=png2, anchor=NW)
    if k == 0: #Вывод информации о результате хода
        n += 1
        sms2.config(text=sms2.cget('text') + str(n) + '. Ваше число: ' + y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы\n')
        Entry.delete(0, END)
    else:
        k = 0
        Entry.delete(0, END)
    if n > 15: #То, что будет происходить при поражении
        messagebox.showinfo('Поражение', 'Вы не смогли отгадать число, им было: ' + x)
        answer2 = messagebox.askyesno(title='Новая игры', message='Хотите начать новую игру?')
        sms2.config(text='')
        sms2.config(text=sms2.cget('text') + 'Загаданным числом было : ' + x + '\n Было затраченно: ' + str(n) + ' ходов \n ')
        if answer2:
            x = ''
            n = 0
            sms2.config(text='Бык - цифра на своём месте.\n'
                        'Корова - цифра не на своём месте.')
            can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can.place(x=0, y=50)
            can.create_image(0, 0, image=png3, anchor=NW)
            can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can2.place(x=0, y=200)
            can2.create_image(0, 0, image=png3, anchor=NW)
            can3 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can3.place(x=0, y=350)
            can3.create_image(0, 0, image=png3, anchor=NW)
            can4 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can4.place(x=0, y=500)
            can4.create_image(0, 0, image=png3, anchor=NW)
            can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can5.place(x=615, y=50)
            can5.create_image(0, 0, image=png3, anchor=NW)
            can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can6.place(x=615, y=200)
            can6.create_image(0, 0, image=png3, anchor=NW)
            can7 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can7.place(x=615, y=350)
            can7.create_image(0, 0, image=png3, anchor=NW)
            can8 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can8.place(x=615, y=500)
            can8.create_image(0, 0, image=png3, anchor=NW)
        else:
            Entry.unbind('<Return>')
            Entry.config(state='disabled')
    if x == y: #То, что будет происходить при победе
        sms2.config(text='')
        sms2.config(text=sms2.cget('text') + 'Загаданным числом было: ' + x + '\nБыло затраченно: ' + str(n) + ' ходов ')
        messagebox.showinfo('Победа!', 'Поздравляем, вы отгадали число.')
        answer = messagebox.askyesno(title='Новая игры', message='Хотите начать новую игру?')
        if answer:
            x = ''
            n = 0
            sms2.config(text='Бык - цифра на своём месте.\n'
                        'Корова - цифра не на своём месте.')
            can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can.place(x=0, y=50)
            can.create_image(0, 0, image=png3, anchor=NW)
            can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can2.place(x=0, y=200)
            can2.create_image(0, 0, image=png3, anchor=NW)
            can3 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can3.place(x=0, y=350)
            can3.create_image(0, 0, image=png3, anchor=NW)
            can4 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can4.place(x=0, y=500)
            can4.create_image(0, 0, image=png3, anchor=NW)
            can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can5.place(x=615, y=50)
            can5.create_image(0, 0, image=png3, anchor=NW)
            can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can6.place(x=615, y=200)
            can6.create_image(0, 0, image=png3, anchor=NW)
            can7 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can7.place(x=615, y=350)
            can7.create_image(0, 0, image=png3, anchor=NW)
            can8 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
            can8.place(x=615, y=500)
            can8.create_image(0, 0, image=png3, anchor=NW)
        else:
            Entry.unbind('<Return>')
            Entry.config(state='disabled')

def new_game(): #Функция начала новой игры
    global n, x
    answer3 = messagebox.askyesno(title='Новая игра', message='Вы уверены что хотите начать новую игру?')
    if answer3:
        n = 0
        x = ''
        sms2.config(text='Бык - цифра на своём месте.\n'
                        'Корова - цифра не на своём месте.')
        Entry.config(state='normal')
        Entry.bind('<Return>', play)
        can = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can.place(x=0, y=50)
        can.create_image(0, 0, image=png3, anchor=NW)
        can2 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can2.place(x=0, y=200)
        can2.create_image(0, 0, image=png3, anchor=NW)
        can3 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can3.place(x=0, y=350)
        can3.create_image(0, 0, image=png3, anchor=NW)
        can4 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can4.place(x=0, y=500)
        can4.create_image(0, 0, image=png3, anchor=NW)
        can5 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can5.place(x=615, y=50)
        can5.create_image(0, 0, image=png3, anchor=NW)
        can6 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can6.place(x=615, y=200)
        can6.create_image(0, 0, image=png3, anchor=NW)
        can7 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can7.place(x=615, y=350)
        can7.create_image(0, 0, image=png3, anchor=NW)
        can8 = Canvas(bg='gray22', width=200, height=200, highlightthickness=0)
        can8.place(x=615, y=500)
        can8.create_image(0, 0, image=png3, anchor=NW)

png =  PhotoImage(file='bik.png')
png2 = PhotoImage(file='korova.png')
png3 = PhotoImage(file='gray22.png')
png4 = PhotoImage(file='21.png')

label1 = tkinter.Label(text='Быки и коровы', font='Courier 25', bg='gray22', fg='white') #Вывод названия игры
label1.pack(anchor=N)

buttonExample = tkinter.Button(root, #Кнопка открытия правил
              text="Открыть правила",
              command=createNewWindow, bg='grey', fg='white', width=20, font='Helvetica 9')
buttonExample.pack(anchor=S, pady=10, ipadx=10, ipady=10)

buttonnewgame = tkinter.Button(root, text='Новая игра', command=new_game, bg='grey', fg='blue', width=20, font='Helvetica 9') #Кнопка новой игры
buttonnewgame.pack(anchor=S, pady=10, ipadx=10, ipady=10)

buttonexit = tkinter.Button(root, #Кнопка закрытия приложения
                      text='Закрыть приложение',
                      command=on_closing, bg='grey', fg='red', width=20, font='Helvetica 9')
buttonexit.pack(anchor=S, pady=10, ipadx=10, ipady=10)

Entry = Entry(width=20, font=("Times", 15, "bold"), justify='center') #Поле для ввода числа
Entry.pack(pady=5, ipadx=5, ipady=7)
Entry.focus()
Entry.bind( '<Return>', play) #Привязка кнопки Enter, а так же основной игровой функции к полю Entry

sms2 = Message(width=600, padx=10, pady=10, justify="center", #Поле для вывода результатов хода
              text='Бык - цифра на своём месте.\n'
               'Корова - цифра не на своём месте.\n', bg='gray22', fg='white')
sms2.pack(anchor=N, pady=5)
sms2.config(font=('times', 14))

root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Быки и коровы')
root.resizable(False, False)
root.wm_attributes('-topmost', 1)

root.mainloop()