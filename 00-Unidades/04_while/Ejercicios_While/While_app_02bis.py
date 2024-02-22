import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Alan
apellido: del Canto
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        iteration = 0 
        numberSum = 0

        while iteration < 11:
            if iteration % 2 == 0:
                numberSum += iteration
                
            iteration += 1

        alert("Números pares", f"La suma de los números pares entre el 1 y el 10 es de {numberSum}")
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()