from tkinter import *
from pymongo import MongoClient


# post

def post():

    nota = {
        'origem': origem.get(),
        'valor': valor.get(),
        'data': data.get()
    }

    statusLabel['text'] = origem.get() + ' - ' + valor.get() + '$ (' + data.get() + ') - Enviado'

    origemEntry.delete(0, END)
    valorEntry.delete(0, END)
    dataEntry.delete(0, END)

    notas.insert_one(nota)


# mongoDB

client = MongoClient('')
db = client['registro-de-entrada']
notas = db['comprovantes']


# GUI

root = Tk()
root.title('Envio')
root.geometry('300x130')

tituloLabel = Label(root, text='Dados do comprovante')
tituloLabel.grid(column=1, row=0)

origemLabel = Label(root, text='Origem: ')
origemLabel.grid(column = 0, row = 1)
origem = StringVar()
origemEntry = Entry(root, width = 30, textvariable = origem)
origemEntry.grid(column = 1, row = 1)

valorLabel = Label(root, text='Valor: ')
valorLabel.grid(column = 0, row = 2)
valor = StringVar()
valorEntry = Entry(root, width = 30, textvariable = valor)
valorEntry.grid(column = 1, row = 2)

dataLabel = Label(root, text='Data (entrada): ')
dataLabel.grid(column = 0, row = 3)
data = StringVar()
dataEntry = Entry(root, width = 30, textvariable = data)
dataEntry.grid(column = 1, row = 3)

button = Button(root, text = 'Enviar comprovante.', command=post)
button.grid(column = 1, row = 4)

statusLabel = Label(root, text = '')
statusLabel.grid(column=1, row=5)

root.mainloop()