import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        positiveNumbersSum = 0
        positiveNumbersCounter =0

        negativeNumbersSum = 0
        negativeNumbersCounter = 0

        zeroCounter = 0

        while True:
            number = prompt("Número", "Ingrese un número")
            
            if number == None:
                break
            
            number = int(number)

            if number > 0:
                positiveNumbersSum += number
                positiveNumbersCounter += 1

            elif number < 0:
                negativeNumbersSum += number
                negativeNumbersCounter += 1
            
            else:
                zeroCounter += 1

        numberDifference = positiveNumbersSum - negativeNumbersSum


        message = f'''
        La suma acumulada de los números negativos es de {negativeNumbersSum}.
        La suma acumulada de los números positivos es de {positiveNumbersSum}.
        La cantidad de números positivos ingresados es de {positiveNumbersCounter}.
        La cantidad de números negativos ingresados es de {negativeNumbersCounter}.
        La cantidad de ceros ingresados es de {zeroCounter}.
        La diferencia de cantidad entre números positivos y negativos es de {numberDifference}.
        '''         
        alert("Información", message)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
