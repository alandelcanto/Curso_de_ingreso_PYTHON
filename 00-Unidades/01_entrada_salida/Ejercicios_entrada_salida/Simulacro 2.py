import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: Simulacro 2
---
Enunciado:
La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
el costo por millón de kilómetros es de 8 bitcoin 

podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
podes elegir si viajar en verano, primavera  otoño o invierno.

para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%


'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Destino")
        self.label1.grid(row=1, column=0, padx=20, pady=10)

        destinations = ['Luna', 'Titan', 'Marte']
        self.combobox_destinations = customtkinter.CTkComboBox(master=self, values=destinations)
        self.combobox_destinations.grid(row=1, column=1, padx=20, pady=(10, 10))

        self.label2 = customtkinter.CTkLabel(master=self, text="Estación")
        self.label2.grid(row=2, column=0, padx=20, pady=10)

        seasons = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_seasons = customtkinter.CTkComboBox(master=self, values=seasons)
        self.combobox_seasons.grid(row=2, column=1, padx=20, pady=(10, 10))

        self.label3 = customtkinter.CTkLabel(master=self, text="Pasajeros")
        self.label3.grid(row=3, column=0, padx=20, pady=10)

        self.combobox_passengers = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_passengers.grid(row=3, column=1, padx=10, pady=10)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        destination = self.combobox_destinations.get()

        season = self.combobox_seasons.get()

        passengers = self.combobox_passengers.get()
        passengers = int(passengers)

        pricePerMKm = 8

        firstModifier = 0
        secondModifier = 0

        if passengers > 5:
            match(destination):
                case "Luna":
                    firstModifier = 40
                case "Marte":
                    firstModifier = 50
                case "Titan":
                    firstModifier = 30
        
        
        match(destination):
            case "Luna":
                distance = 0.5
                match(season):
                    case "Verano":
                        secondModifier = 15
                    case "Otoño" | "Primavera":
                        secondModifier = 25

            case "Marte":
                distance = 60
                match(season):
                    case "Verano":
                        secondModifier = 10
                    case "Otoño" | "Primavera":
                        secondModifier = 25

            case "Titan":
                distance = 1300
                match(season):
                    case "Verano":
                        secondModifier = 10
                    case "Otoño" | "Primavera":
                        secondModifier = 20
        
        basePrice = pricePerMKm * distance
        firstPrice = basePrice * (1 - firstModifier / 100)
        finalPrice = firstPrice * (1 - secondModifier / 100)

        finalPrice *= passengers

        finalPrice = round(finalPrice, 2)

        message = f"El precio total por un viaje de {distance} millones de Km a {destination} con {passengers} pasajeros en {season} es de {finalPrice} Bitcoin"
        alert("Informe de Viaje", message)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
