import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: entrada_salida_01
---
Enunciado

para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  "

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        price = 1000

        nameA = prompt("Ingrese nombre", "Ingrese el nombre de la primera persona")
        nameB = prompt("Ingrese nombre", "Ingrese el nombre de la segunda persona")

        ageA = prompt("Ingrese edad", "Ingrese la edad de la primera persona")
        ageA = int(ageA)

        ageB = prompt("Ingrese edad", "Ingrese la edad de la segunda persona")
        ageB = int(ageB)

        weightA = prompt("Ingrese peso", "Ingrese el peso de la primera persona")
        weightA = int(weightA)

        weightB = prompt("Ingrese peso", "Ingrese el peso de la segunda persona")
        weightB = int(weightB)


        weightSum = weightA + weightB

        ageParsed = (ageA + ageB) / 2

        totalCost = weightSum * price


        message = f"Hola {nameA} y {nameB}, sus pesos son {weightA} kilos y {weightB} kilos respectivamente, con un peso total de {weightSum} y una edad promedio de {ageParsed}. El costo total de su viaje es de ${totalCost}"
        alert("Información de Viaje", message)    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
