import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
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

        counter = 0

        for i in range(1, endValue):
            if endValue % i == 0:
                print(i)
                counter += 1

        alert("Cantidad de divisores", f"Se encontraron {counter} números divisores")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()