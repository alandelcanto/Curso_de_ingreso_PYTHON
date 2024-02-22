import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''



class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        firstDataCounter = 0
        minimumAge = 0

        genderFCounter = 0
        genderMCounter = 0
        genderNBCounter = 0

        genderFAgeSum = 0
        genderMAgeSum = 0
        genderNBAgeSum = 0

        counterPYTHON = 0
        counterJS = 0
        counterASPNET = 0

        minimumAgeName = ""

        for i in range(2):
            name = prompt("Ingrese datos", "Ingrese el nombre del postulante")

            age = prompt("Ingrese datos", "Ingrese la edad del postulante")
            age = int(age)

            while age < 18:
                age = prompt("Reingrese datos", "Reingrese la edad del postulante")
                age = int(age)
                if minimumAge == 0:
                    minimumAge = age

            

            gender = prompt("Ingrese datos", "Ingrese el género del postulante")

            while gender != "F" and gender != "M" and gender != "NB":
                gender = prompt("Reingrese datos", "Reingrese el género del postulante")

            programmingLanguage = prompt("Ingrese datos", "Ingrese la tecnología del postulante")

            while programmingLanguage != "PYTHON" and programmingLanguage != "JS" and programmingLanguage != "ASP.NET":
                programmingLanguage = prompt("Reingrese datos", "Reingrese la tecnología del postulante")

            jobPosition = prompt("Ingrese datos", "Ingrese la posición del postulante")

            while jobPosition != "Jr" and jobPosition != "Ssr" and jobPosition != "Sr":
                jobPosition = prompt("Reingrese datos", "Reingrese la posición del estudiante")

            #A

            if gender == "NB" and (programmingLanguage == "JS" or programmingLanguage == "ASP.NET") and 25 <= age <= 40 and jobPosition == "Ssr":
                firstDataCounter += 1

            #B

            if jobPosition == "Jr" and (age < minimumAge):
                minimumAge = age
                minimumAgeName = name

            #C

            if gender == "F":
                genderFCounter += 1
                genderFAgeSum += age
            elif gender == "M":
                genderMCounter += 1
                genderMAgeSum += age
            else:
                genderNBCounter += 1
                genderNBAgeSum += age

            #D
                
            if programmingLanguage == "PYTHON":
                counterPYTHON += 1
            elif programmingLanguage == "JS":
                counterJS += 1
            else:
                counterASPNET += 1
        #C
        if genderMCounter != 0 : 
            genderMAverage = genderMAgeSum / genderMCounter
        if genderFCounter != 0 :
            genderFAverage = genderFAgeSum / genderFCounter
        if genderNBCounter != 0 :
            genderNBAverage = genderNBAgeSum / genderNBCounter

        #D
        if counterPYTHON > counterJS and counterPYTHON > counterASPNET:
            popularProgrammingLanguage = "PYTHON"
        elif counterJS > counterASPNET:
            popularProgrammingLanguage = "JS"
        else:
            popularProgrammingLanguage = "ASP.NET"

        #E
        genderTotalCounter = genderFCounter + genderMCounter + genderNBCounter

        genderMPercent = (genderMCounter / genderTotalCounter) * 100
        genderFPercent = (genderFCounter / genderTotalCounter) * 100
        genderNBPercent = (genderNBCounter / genderTotalCounter) * 100

        print(f"La cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr es de {firstDataCounter}")
        
        print(f"El postulante Jr más joven es {minimumAgeName}")

        print(f"El promedio de edad de postulantes hombres es de {genderMAverage} años")
        print(f"El promedio de edad de postulantes mujeres es de {genderFAverage} años")
        print(f"El promedio de edad de postulantes no binarios es de {genderNBAverage} años")

        print(f"La tecnología con más postulantes es {popularProgrammingLanguage}")

        print(f"Los postulantes hombres representan un {genderMPercent}% del total")
        print(f"Las postulantes mujeres representan un {genderFPercent}% del total")
        print(f"Los postulantes no binarios representan un {genderNBPercent}% del total")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
