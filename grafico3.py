import tkinter as Tk

def suma():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="Resultado: " + str(resultado))

def resta():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text="Resultado: " + str(resultado))

def multi():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text="Resultado: " + str(resultado))

def div():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 / num2
    label_resultado.config(text="Resultado: " + str(resultado))

def insert_number(number):
    current_entry = app.focus_get()
    if isinstance(current_entry, Tk.Entry):
        current_entry.insert(Tk.END, number)

def clear_all():
    entry_num1.delete(0, Tk.END)
    entry_num2.delete(0, Tk.END)
    label_resultado.config(text="Resultado: ")

app = Tk.Tk()
app.title("CALCULADORA")

label_num1 = Tk.Label(text="Primer valor")
entry_num1 = Tk.Entry()

label_num2 = Tk.Label(text="Segundo valor")
entry_num2 = Tk.Entry()

#Resultado
label_resultado = Tk.Label(text="Resultado: ", relief="sunken", width=20)

button_suma = Tk.Button(text="Sumar", command=suma, width=10, height=1)
button_resta = Tk.Button(text="Resta", command=resta, width=10, height=1)
button_multi = Tk.Button(text="Multiplicar", command=multi, width=10, height=1)
button_div = Tk.Button(text="Dividir", command=div, width=10, height=1)
button_ac = Tk.Button(text="AC", command=clear_all, width=10, height=1)

button_n0 = Tk.Button(text="0", command=lambda: insert_number("0"), width=3, height=1)
button_n1 = Tk.Button(text="1", command=lambda: insert_number("1"), width=3, height=1)
button_n2 = Tk.Button(text="2", command=lambda: insert_number("2"), width=3, height=1)
button_n3 = Tk.Button(text="3", command=lambda: insert_number("3"), width=3, height=1)
button_n4 = Tk.Button(text="4", command=lambda: insert_number("4"), width=3, height=1)
button_n5 = Tk.Button(text="5", command=lambda: insert_number("5"), width=3, height=1)
button_n6 = Tk.Button(text="6", command=lambda: insert_number("6"), width=3, height=1)
button_n7 = Tk.Button(text="7", command=lambda: insert_number("7"), width=3, height=1)
button_n8 = Tk.Button(text="8", command=lambda: insert_number("8"), width=3, height=1)
button_n9 = Tk.Button(text="9", command=lambda: insert_number("9"), width=3, height=1)

# Usando el método place para posicionar los widgets
label_num1.place(x=50, y=170)
entry_num1.place(x=50, y=150)
label_num2.place(x=200, y=170)
entry_num2.place(x=200, y=150)
button_suma.place(x=350, y=30)
button_resta.place(x=350, y=70)
button_multi.place(x=350, y=110)
button_div.place(x=350, y=150)
button_ac.place(x=350, y=190)
label_resultado.place(x=50, y=200)

# Botones de los números
button_n0.place(x=50, y=40)
button_n1.place(x=90, y=40)
button_n2.place(x=130, y=40)
button_n3.place(x=170, y=40)
button_n4.place(x=210, y=40)
button_n5.place(x=50, y=90)
button_n6.place(x=90, y=90)
button_n7.place(x=130, y=90)
button_n8.place(x=170, y=90)
button_n9.place(x=210, y=90)

app.geometry("500x300")
app.mainloop()
