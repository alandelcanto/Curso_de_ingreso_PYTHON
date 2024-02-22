import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
TP: Match_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        unitPrice = 800
        discount = 0

        quantity = self.combobox_cantidad.get()
        quantity = int(quantity)

        brand = self.combobox_marca.get()

        
        match(quantity):
            case 5:
                match(brand):
                    case "ArgentinaLuz":
                        discount = 40
                    case _:
                        discount = 30
            case 4:
                match(brand):
                    case "ArgentinaLuz" | "FelipeLamparas":
                        discount = 25
                    case _:
                        discount = 20
            case 3:
                match(brand):
                    case "ArgentinaLuz":
                        discount = 15
                    case "FelipeLamparas":
                        discount = 10
                    case _:
                        discount = 5
            case 2 | 1 :
                pass
            case _:
                discount = 50

        subTotal = quantity * unitPrice
        total = subTotal * (1 - discount / 100)

        if total > 4000:
            discount += 5
            total = subTotal * (1 - discount / 100)

        total = round(total)


        message = f"El importe total de su compra de {quantity} lámparas de bajo consumo de marca {brand} es de ${total}, considerando un descuento del {discount}% de un total sin descontar de ${subTotal}, calculado según sus opciones de compra."
        alert("Informe de Compra", message)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()