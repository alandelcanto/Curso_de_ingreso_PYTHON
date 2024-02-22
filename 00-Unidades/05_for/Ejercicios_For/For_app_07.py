import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        endValue = prompt("Número", "Ingrese un número")
        endValue = int(endValue)

        primeNumberFlag = True

        for i in range(2, endValue):
            if endValue % i == 0:
                primeNumberFlag = False
                break

        if primeNumberFlag == True:
            message = "Es un número primo"
        else:
            message = "NO es un número primo"

        alert("Número primo", message)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()