import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


""" 
Simulacro 01 - Dr. UTN

Nombre: Alan
Apellido: del Canto

Enunciado:

De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    ● Nombre 
    ● Temperatura, entre 35 y 42
    ● Sexo( f, m , nb )
    ● Edad(mayor a 0)

Pedir datos por Prompt y mostrar por Print

Punto A - por el número de DNI del alumno:


DNI terminados en 0 o 1

1) Informar la cantidad de personas de sexo femenino
2) La edad promedio de personas de sexo masculino
3) El nombre de la persona la persona de sexo nb con más temperatura(si la hay)

DNI terminados en 2 o 3
1) Informar la cantidad de personas de sexo masculino
2) La edad promedio de personas de sexo nb
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

DNI terminados en 4 o 5
1) Informar la cantidad de personas de sexo nb
2) La edad promedio de personas de sexo femenino
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 6 o 7
1) Informar la cantidad de personas mayores de edad (desde los 18 años)
2) La edad promedio en total de todas las personas mayores de edad (18 años)
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 8 o 9
1) Informar la cantidad de personas menores de edad (menos de 18 años)
2) La temperatura promedio en total de todas las personas menores de edad
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)


Todos los alumnos:
B - Informar cual fue el sexo mas ingresado
C - El porcentaje de personas con fiebre y el porcentaje sin fiebre
"""



class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        genderMCounter = 0
        genderFCounter = 0
        genderNBCounter = 0

        genderFAgeSum = 0
        genderMAgeSum = 0
        genderNBAgeSum = 0  
        adultAgeSum = 0
        minorAgeSum = 0

        genderMMinimumTemperature = 0
        genderMMinimumTemperatureName = ""
        genderMMinimumTemperatureFlag = False

        genderFMinimumTemperature = 0
        genderFMinimumTemperatureName = ""
        genderFMinimumTemperatureFlag = False

        genderNBMinimumTemperature = 0
        genderNBMinimumTemperatureName = ""
        genderNBMinimumTemperatureFlag = False

        feverPatientsCounter = 0
        nonFeverPatientsCounter = 0

        totalPatientCounter = 0

        feverPatientsPercent = 0
        nonFeverPatientsPercent = 0
        genderFAgeAverage = 0
        genderMAgeAverage = 0
        genderNBAgeAverage = 0

        adultAgeAverage = 0
        minorAgeAverage = 0

        messageFirst = ""
        messageFinal = ""

        adultCounter = 0
        minorCounter = 0

        for i in range (5):

            name = prompt("Ingrese datos", "Ingrese el nombre del paciente")
            if name == None:
                break
            elif name.isalpha() != True:
                name = prompt("Reingrese datos", "Reingrese el nombre del paciente")
            
            temperature = prompt("Ingrese datos", "Ingrese la temperatura del paciente (35° - 42°)")
            if temperature == None:
                break
            elif temperature.isdigit() == True:
                temperature = float(temperature)
            else:
                temperature = 0

            while temperature < 35 or temperature > 42:
                temperature = prompt("Reingrese datos", "Reingrese la temperatura del paciente (35° - 42°)")
                if temperature == None:
                    break
                elif temperature.isdigit() == True:
                    temperature = float(temperature)
                else:
                    temperature = 0

            gender = prompt("Ingrese datos", "Ingrese el género del paciente (F - M - NB)")
            if gender == None:
                break
            elif gender.isalpha() != True:
                gender = "ERROR"

            while gender != "F" and gender != "M" and gender != "NB":
                gender = prompt("Reingrese datos", "Reingrese el género del paciente (F - M - NB)")
                if gender == None:
                    break
                elif gender.isalpha() != True:
                    gender = "ERROR"

            age = prompt("Ingrese datos", "Ingrese la edad del paciente")
            if age == None:
                break
            elif age.isdigit() == True:
                age = int(age)
            else:
                age = 0

            while age <= 0:
                age = prompt("Reingrese datos", "Reingrese la edad del paciente")
                if age == None:
                    break
                elif age.isdigit() == True:
                    age = int(age)
                else:
                    age = 0
            ####
            #Información por paciente para revisar si se ingresaron los datos correctos
            messageFirst += ("INFORMACIÓN DE PACIENTE\n")
            messageFirst += (f"El nombre del paciente N°{i + 1} es {name}\n")
            messageFirst += (f"Su género es {gender}\n")
            messageFirst += (f"Tiene {age} años\n")
            messageFirst += (f"Tiene {temperature} grados de temperatura\n")
            print(messageFirst)
            ####
            totalPatientCounter += 1
                
            match gender: #Variables gobernadas por género
                case "F":
                    genderFCounter += 1

                    genderFAgeSum += age

                    if genderFMinimumTemperature > temperature or genderFMinimumTemperatureFlag == False:
                        genderFMinimumTemperature = temperature
                        genderFMinimumTemperatureName = name
                        genderFMinimumTemperatureFlag = True
                case "M":
                    genderMCounter += 1

                    genderMAgeSum += age

                    if genderMMinimumTemperature > temperature or genderMMinimumTemperatureFlag == False:
                        genderMMinimumTemperature = temperature
                        genderMMinimumTemperatureName = name
                        genderMMinimumTemperatureFlag = True

                case "NB":
                    genderNBCounter += 1

                    genderNBAgeSum += age

                    if genderNBMinimumTemperature > temperature or genderNBMinimumTemperatureFlag == False:
                        genderNBMinimumTemperature = temperature
                        genderNBMinimumTemperatureName = name
                        genderNBMinimumTemperatureFlag = True

            if temperature > 37: #Contador de fiebre
                feverPatientsCounter += 1
            else:
                nonFeverPatientsCounter += 1
            
            if age >= 18:
                adultCounter += 1

                adultAgeSum += age
            else:
                minorCounter += 1

                minorAgeSum += age

        

        ####
        if genderFCounter != 0: #Promedio de femeninos
            genderFAgeAverage = genderFAgeSum / genderFCounter
        if genderMCounter != 0:
            genderMAgeAverage = genderMAgeSum / genderMCounter
        if genderNBCounter != 0:
            genderNBAgeAverage = genderNBAgeSum / genderNBCounter
        
        if adultCounter != 0:
            adultAgeAverage = adultAgeSum / adultCounter
        if minorCounter != 0:
            minorAgeAverage = minorAgeSum / minorCounter


        if genderMCounter > genderFCounter and genderMCounter > genderNBCounter: #Calcula mayoría de un género
            mostPatientsGender = "Masculino"
            mostPatientsGenderCounter = genderMCounter
        elif genderFCounter > genderNBCounter:
            mostPatientsGender = "Femenino"
            mostPatientsGenderCounter = genderFCounter
        else:
            mostPatientsGender = "No binario"
            mostPatientsGenderCounter = genderNBCounter

        if totalPatientCounter > 0: #Porcentaje de fiebre
            feverPatientsPercent = (feverPatientsCounter / totalPatientCounter) * 100
            nonFeverPatientsPercent = 100 - feverPatientsPercent

        feverPatientsPercent = round(feverPatientsPercent)
        nonFeverPatientsPercent = round(nonFeverPatientsPercent)

        genderFAgeAverage = round(genderFAgeAverage, 1)
        genderMAgeAverage = round(genderMAgeAverage, 1)
        genderNBAgeAverage = round(genderNBAgeAverage, 1)

        adultAgeAverage = round(adultAgeAverage, 1)
        minorAgeAverage = round(minorAgeAverage, 1)

        ####
        if totalPatientCounter != 0:
            messageFinal += (f"La cantidad de personas masculinas es de {genderMCounter}\n")

            messageFinal += (f"La cantidad de personas femeninas es de {genderFCounter}\n")

            messageFinal += (f"La cantidad de personas no binarias es de {genderNBCounter}\n")

            messageFinal += (f"La cantidad de personas mayores de edad es de {adultCounter}\n")

            messageFinal += (f"La cantidad de personas menores de edad es de {minorCounter}\n")

            messageFinal += (f"El promedio de edad de los pacientes masculinos es de {genderMAgeAverage} años\n")

            messageFinal += (f"El promedio de edad de los pacientes femeninos es de {genderFAgeAverage} años\n")

            messageFinal += (f"El promedio de edad de los pacientes no binarios es de {genderNBAgeAverage} años\n")
            
            messageFinal += (f"El promedio de edad de los pacientes mayores de edad es de {adultAgeAverage} años\n")
            
            messageFinal += (f"El promedio de edad de los pacientes menores de edad es de {minorAgeAverage} años\n")

            if genderMCounter > 0:
                messageFinal += (f"El paciente masculino con la menor temperatura es {genderMMinimumTemperatureName} con {genderMMinimumTemperature} grados\n") 
            else:
                messageFinal += (f"No hubo paciente masculinos\n")

            if genderFCounter > 0:
                messageFinal += (f"El paciente femenino con la menor temperatura es {genderFMinimumTemperatureName} con {genderFMinimumTemperature} grados\n") 
            else:
                messageFinal += (f"No hubo paciente femeninos\n")

            if genderNBCounter > 0:
                messageFinal += (f"El paciente no binario con la menor temperatura es {genderNBMinimumTemperatureName} con {genderNBMinimumTemperature} grados\n") 
            else:
                messageFinal += (f"No hubo paciente no binarios\n")
            
            messageFinal += (f"La mayoría de los pacientes son de género {mostPatientsGender}, con un total de {mostPatientsGenderCounter} pacientes\n") #B

            messageFinal += (f"El {feverPatientsPercent}% de los pacientes tiene fiebre, mientras que el {nonFeverPatientsPercent}% no tiene fiebre\n") #C

        else:
            messageFinal += (f"No hubo pacientes\n")

        print(messageFinal)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
