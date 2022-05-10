from tkinter import *
janela = Tk()
janela.title('Boas vindas')
texto = Label(janela, text='Olá Mundo')
texto.grid(columnspan=3, row=3)
janela.mainloop()
