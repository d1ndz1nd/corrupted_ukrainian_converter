from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser

root = Tk()
root.geometry('400x320')
root.resizable(False, False)
root.title("Виправлення розкладки")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

user_text_variable = ''

def user_entry():
    global user_text_variable
    user_text = entry_user_text.get()
    if user_text != '' and user_text != user_text_variable:
        converted_text_list = []
        ukr_symbols = {
            'q':'й',
            'w':'ц',
            'e':'у',
            'r':'к',
            't':'е',
            'y':'н',
            'u':'г',
            'i':'ш',
            'o':'щ',
            'p':'з',
            '[':'х',
            '{':'Х',
            ']':'ї',
            '}':'Ї',
            'a':'ф',
            's':'і',
            'd':'в',
            'f':'а',
            'g':'п',
            'h':'р',
            'j':'о',
            'k':'л',
            'l':'д',
            ';':'ж',
            ':':'Ж',
            "'":"є",
            '"':'Є',
            'z':'я',
            'x':'ч',
            'c':'с',
            'v':'м',
            'b':'и',
            'n':'т',
            'm':'ь',
            ',':'б',
            '<':'Б',
            '.':'ю',
            '>':'Ю',
            '/':'.',
            ' ':' ',
            }
        for ch in user_text:
            lower_ch = ch.lower()
            if lower_ch in ukr_symbols:
                new_char = ukr_symbols[lower_ch]
                if ch.isupper():
                    new_char = new_char.upper()
                converted_text_list.append(new_char)
            else:
                converted_text_list.append(ch)
        converted_text = "".join(converted_text_list)
        user_text_variable = user_text
        
        entry_converted_text.config(state='normal')
        entry_converted_text.delete(0, END)
        entry_converted_text.insert(0, converted_text)
        entry_converted_text.config(state='readonly')
    else:
        messagebox.showerror(
                'Помилка',
                'Введіть новий текст у рядок, а потім натисніть кнопку "Конвертувати"'
            )
    

def open_link(event):
    webbrowser.open('https://github.com/d1ndz1nd/corrupted_ukrainian_converter')

def copy_text():
    text = entry_converted_text.get()
    if text != '':
        root.clipboard_clear()      
        root.clipboard_append(text)
    else:
        messagebox.showerror(
                'Помилка',
                'Кнопка "Копіювати" доступна тільки після виконання конвертування тексту'
            )

def entry_clear():
    entry_user_text.delete(0, END)
    entry_converted_text.config(state='normal')
    entry_converted_text.delete(0, END)
    entry_converted_text.config(state='readonly')

    
label_user_entry = Label(root, text='Введіть ваш пошкоджений український текст:')
label_user_entry.pack(pady=10)

entry_user_text = Entry(root, width=50)
entry_user_text.pack(padx=10,pady=5)

buttons_frame = Frame(root)
buttons_frame.pack(pady=5)

button_user_entry = Button(buttons_frame, text='Конвертувати', command=user_entry)
button_user_entry.pack(side=LEFT, padx=5)

button_entry_clear = Button(buttons_frame, text='Очистити', command=entry_clear)
button_entry_clear.pack(side=LEFT, padx=5)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

label_converted_entry = Label(root, text='Ваш виправлений текст:')
label_converted_entry.pack(pady=10)

entry_converted_text = Entry(root, width=50)
entry_converted_text.pack(padx=10,pady=5)
entry_converted_text.config(state='readonly')

button_copy_converted_entry = Button(root, text='Скопіювати', command=copy_text)
button_copy_converted_entry.pack(padx=10,pady=5)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

label_open_source = Label(root, text='Вихідний код програми', fg='blue', cursor='hand2')
label_open_source.pack()
label_open_source.bind("<Button-1>", open_link)

root.mainloop()
