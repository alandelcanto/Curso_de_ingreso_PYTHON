import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import time
'''
nombre: Alan
apellido: del Canto
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''
cache = {}


class App(customtkinter.CTk):

  
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        start = time.time()
        endValue = prompt("Número", "Ingrese un número")
        endValue = int(endValue)

        primeCounter = 0
        primeNumberFlag = True

        i = 0
        j = 0

        for i in range(2, endValue):
            primeNumberFlag = True

            for j in range(2, i):
                if cache.get(i) != None:
                    break
                elif i % j == 0 :
                    primeNumberFlag = False
                    break
                if (i / 2)  < j:
                   break
                
                    
            if primeNumberFlag == True:
                primeCounter +=1
                cache.update({i:j})
                
        print(time.time() - start)
        alert("Números primos", f"Se encontraron {primeCounter} números primos")






    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()