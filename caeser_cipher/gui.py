import tkinter as tk
from tkinter import filedialog, messagebox, Button

from cipher import *
from valident import *

class AppGui:
    def __init__(self):
        #главное окно
        self.root = tk.Tk()
        self.root.title("Шифратор")

        tk.Label(text='исходный текст: ').pack()
        self.input_text = tk.Text(height= 7, width= 70)
        self.input_text.pack()

        tk.Label(text='ключ: ').pack()
        self.key_entry = tk.Entry()
        self.key_entry.pack()

        self.mode = tk.StringVar(value='encrypt')
        tk.Radiobutton(text = 'зашифровать', variable = self.mode, value = 'encrypt').pack()
        tk.Radiobutton(text = 'дешифровать', variable = self.mode, value = 'decrypt').pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady = 5)
        tk.Button(button_frame, text = 'выполнить', command = self.start).pack(side = 'left', padx = 5, pady = 5)
        tk.Button(button_frame, text = 'очистить', command = self.clear).pack(side = 'left', padx = 5, pady = 5)

        tk.Label(text = 'результат').pack()
        self.output_text = tk.Text(height= 7, width= 70)
        self.output_text.pack()

    #кнопка выполнить
    def start(self):
        text = self.input_text.get("1.0", 'end').strip()
        key_str = self.key_entry.get()

        if not text:
            messagebox.showerror("Ошибка", "Введите текст для шифрования или дешифрования!")
            return

        try:
            key = v_key(key_str)
            result = cipher(text, key, self.mode.get())

            self.output_text.delete('1.0', 'end')
            self.output_text.insert('1.0', result)

        except Exception as e:
            messagebox.showerror('ошибка', str(e))

    #очистить
    def clear(self):
        self.input_text.delete('1.0', 'end')
        self.output_text.delete('1.0', 'end')
        self.key_entry.delete(0, 'end')

    def run(self):
        self.root.mainloop()