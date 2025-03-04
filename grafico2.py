import tkinter as Tk #alias Tk

def suma():
    num1=int(entry_num1.get()) #entry_num1 es una caja de texto1
    num2=int(entry_num2.get()) #entry_num2 es una caja de texto2
    resultado=num1 + num2
    label_resultado.config(text="resultado:" + str(resultado)) #asigna 
def resta():  
    num1=int(entry_num1.get()) #entry_num1 es una caja de texto1
    num2=int(entry_num2.get()) #entry_num2 es una caja de texto2
    resultado=num1 - num2
    label_resultado.config(text="resultado:" + str(resultado)) #asigna 
def multiplicacion():
    num1=int(entry_num1.get()) #entry_num1 es una caja de texto1
    num2=int(entry_num2.get()) #entry_num2 es una caja de texto2
    resultado=num1 * num2
    label_resultado.config(text="resultado:" + str(resultado)) #asigna    
def division ():
    num1=int(entry_num1.get()) #entry_num1 es una caja de texto1
    num2=int(entry_num2.get()) #entry_num2 es una caja de texto2
    resultado=num1 / num2
    label_resultado.config(text="resultado:" + str(resultado)) #asigna  
    
app=Tk.Tk() #ventana o formulario app alias Tk
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC") 

label_num1=Tk.Label(text="primer numero")  # label_num1 es de tipo label 
entry_num1=Tk.Entry() # captar el primer valor

label_num2=Tk.Label(text="segundo numero")  # label_num2 es de tipo label 
entry_num2=Tk.Entry() # captar el segundo  valor 

label_resultado=Tk.Label(text="*****") # label
button_suma=Tk.Button(text="suma" , command=suma) #boton_suma es de tipo boton 

label_resultado=Tk.Label(text="*****") # label
button_resta=Tk.Button(text="resta" , command=resta) #boton_suma es de tipo boton 

label_resultado=Tk.Label(text="*****") # label
button_multiplicacion=Tk.Button(text="multiplicacion" , command=multiplicacion) #boton_suma es de tipo boton 

label_resultado=Tk.Label(text="*****") # label
button_division=Tk.Button(text="division" , command=division) #boton_suma es de tipo boton 

label_num1.pack() #empaquetar y mostrar label_num1 en pantalla 
entry_num1.pack() #empaquetar y mostrar la caja de texto entry_num1 en pantalla 

label_num2.pack() #empaquetar y mostrar label_num2 en pantalla 
entry_num2.pack() #empaquetar y mostrar la caja de texto entry_num2 en pantalla

label_resultado.pack() #empaquetar 
button_suma.pack() #empaquetar y mostrar el boton_suma en pantalla 

label_resultado.pack() #empaquetar 
button_resta.pack() #empaquetar y mostrar el boton_suma en pantalla 

label_resultado.pack() #empaquetar 
button_multiplicacion.pack() #empaquetar y mostrar el boton_suma en pantalla 

label_resultado.pack() #empaquetar 
button_division.pack() #empaquetar y mostrar el boton_suma en pantalla 

app.geometry("580x500") # visualizar la ventana de 500 por 500 pix 
app.mainloop() #ciclo infinito de la ventana 

 