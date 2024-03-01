import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: Final Programación Inicial - Veterinaria
---
Enunciado:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
    Nombre
    Tipo (gato ,perro o exotico)
    Peso ( entre 10 y 80)
    Sexo( F o M )
    Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
    Informe A- Cuál fue el sexo mas ingresado (F o M)
    Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
    Informe C- El nombre de la mascota más pesada
    Informe D- El sexo y nombre del gato más viejo
    Informe E- El promedio de edad de todas las mascotas
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Ejecutar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        cantidadMascotas = 5

        acumuladorEdad = 0

        contadorF = 0
        contadorM = 0

        contadorGato = 0
        contadorPerro = 0
        contadorExotico = 0

        edadMáximaBandera = False
        pesoMáximoBandera = False

        mensajeFinal = ""


        for i in range(cantidadMascotas):
            ##Inputs
            nombre = prompt("Ingrese datos", "Ingrese el nombre de la mascota")

            tipo = prompt("Ingrese datos", "Ingrese el tipo de mascota (Gato - Perro - Exotico)")

            while tipo != "Gato" and tipo != "Perro" and tipo != "Exotico":
                tipo = prompt("Reingrese datos", "Reingrese el tipo de mascota (Gato - Perro - Exotico)")

            peso = prompt("Ingrese datos", "Ingrese el peso de la mascota (10 - 80)")
            if peso != None:
                peso = int(peso)
            else:
                peso = -999

            while peso < 10 or peso > 80:
                peso = prompt("Reingrese datos", "Reingrese el peso de la mascota (10 - 80)")
                if peso != None:
                    peso = int(peso)
                else:
                    peso = -999

            sexo = prompt("Ingrese datos", "Ingrese el sexo de la mascota (F - M)")

            while sexo != "F" and sexo != "M":
                sexo = prompt("Reingrese datos", "Reingrese el sexo de la mascota (F - M)")

            edad = prompt("Ingrese datos", "Ingrese la edad de la mascota")
            if edad != None:
                edad = int(edad)
            else:
                edad = -999

            while edad < 0:
                edad = prompt("Reingrese datos", "Reingrese la edad de la mascota")
                if edad != None:
                    edad = int(edad)
                else:
                    edad = -999

            ##Proceso dentro del loop
            match sexo:
                case "F":
                    contadorF += 1
                case "M":
                    contadorM += 1

            match tipo:
                case "Gato":
                    contadorGato += 1
                case "Perro":
                    contadorPerro += 1
                case "Exotico":
                    contadorExotico += 1

            acumuladorEdad += edad
            
            ##
            
            if pesoMáximoBandera == False: #C
                pesoMáximo = peso
                nombrePesoMáximo = nombre
                pesoMáximoBandera = True
            elif peso > pesoMáximo:
                pesoMáximo = peso
                nombrePesoMáximo = nombre
            
            ##

            if edadMáximaBandera == False: #D
                edadMáxima = edad
                edadMáximaNombre = nombre
                edadMáximaSexo = sexo
                edadMáximaBandera = True
            elif edad > edadMáxima:
                edadMáxima = edad
                edadMáximaNombre = nombre
                edadMáximaSexo = sexo

            ##
            
        ##Proceso fuera del loop
        if contadorM > contadorF: #A
            sexoMayor = "M (Macho)"
            sexoMayorCantidad = contadorM
        else:
            sexoMayor = "F (Hembra)"
            sexoMayorCantidad = contadorF
        
        ##
            
        promedioEdad = acumuladorEdad / cantidadMascotas #E
        promedioEdad = round(promedioEdad, 2)

        porcentajeGato = (contadorGato / cantidadMascotas) * 100  #B
        porcentajePerro = (contadorPerro / cantidadMascotas) * 100 
        porcentajeExotico = (contadorExotico / cantidadMascotas) * 100   

        ##Outputs
            
        mensajeFinal += f"El sexo más ingresado fue {sexoMayor}, con {sexoMayorCantidad} mascotas\n" #A
        mensajeFinal += f"El porcentaje de gatos es de {porcentajeGato}, el de perros es de {porcentajePerro}, y el de exóticos es de {porcentajeExotico}\n" #B
        mensajeFinal += f"La mascota más pesada se llama {nombrePesoMáximo}, con {pesoMáximo} Kg\n" #C
        mensajeFinal += f"La mascota más vieja es {edadMáximaNombre} de sexo {edadMáximaSexo}, con {edadMáxima} años\n" #D
        mensajeFinal += f"El promedio de edad de las mascotas es de {promedioEdad}"

        print(mensajeFinal)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
