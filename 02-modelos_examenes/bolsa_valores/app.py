# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4) = 7

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9. 9-7 = 2

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = ["Pepe", "Paola", "Dardo", "Fatiga", "Maria"]
        self.lista_monto = [20000,30000,40000,50000,60000]
        self.lista_tipo_instrumento = ["CEDEAR","BONOS","MEP","CEDEAR","CEDEAR"]
        self.lista_cantidad_instrumento = [20, 35, 199, 100, 80]
    
    def btn_cargar_datos_on_click(self):
        operationCEDEARCounter = 0
        operationBONOSCounter = 0
        operationMEPCounter = 0
        
        zeroDataRegisterType = ""

        firstDataRegisterType = ""

        secondDataRegisterAmount = 0

        thirdDataRegisterAmount = 0

        fourthDataRegisterName = ""
        fourthDataRegisterCost = 0
        fourthDataRegisterFlag = False

        fifthDataRegisterName = ""
        fifthDataRegisterAmount = 0
        fifthDataRegisterIndex = 0

        sixthDataRegisterName = ""
        sixthDataRegisterCost = 0
        sixthDataRegisterIndex = 0
        sixthDataRegisterFlag = False

        seventhDataRegisterName = ""
        seventhDataRegisterAmount = 0
        seventhDataRegisterIndex = 0

        eighthDataRegisterSum = 0
        eighthDataRegisterAverage = 0

        ninthDataRegisterSum = 0
        ninthDataRegisterAverage = 0

        for i in range(10):
            name = prompt("Ingrese datos", "Ingrese el nombre del usuario") #Input de nombre
            if name == None:
                break

            operationCost = prompt("Ingrese datos", "Ingrese el monto de la operación") #Input de costo de operación
            if operationCost != None:
                operationCost = int(operationCost)
            else:
                break
            while operationCost < 10000: #Verificación
                operationCost = prompt("Reingrese datos", "Reingrese un monto mayor a $10000")
                if operationCost != None:
                    operationCost = int(operationCost)
                else:
                    break

            operationType = prompt("Ingrese datos", "Ingrese si es una operación de CEDEAR, BONOS, o MEP") #Input de tipo de operación
            if operationType == None:
                break
            while operationType != "CEDEAR" and operationType != "BONOS" and operationType != "MEP": #Verificación
                operationType = prompt("Reingrese datos", "Reingrese si es una operación de CEDEAR, BONOS, o MEP")
                if operationType == None:
                    break


            operationCount = prompt("Ingrese datos", "Ingrese el número de elementos comprados") #Input de tipo de operación
            if operationCount != None:
                operationCount = int(operationCount)
            else:
                break
            while operationCount < 0: #Verificación
                operationCount = prompt("Ingrese datos", "Ingrese el número de elementos comprados")
                if operationCount != None:
                    operationCount = int(operationCount)
                else:
                    break


            #0 | 1
            match operationType:
                case "CEDEAR":
                    operationCEDEARCounter += 1
                case "BONOS":
                    operationBONOSCounter += 1
                case _:
                    operationMEPCounter += 1

            #2
            if operationType == "MEP" and 50 <= operationCount <= 200:
                secondDataRegisterAmount += 1

            #3
            if operationType != "CEDEAR":
                thirdDataRegisterAmount += 1

            #4
            if fourthDataRegisterFlag == False and operationType != "MEP":
                fourthDataRegisterName = name
                fourthDataRegisterCost = operationCost
                fourthDataRegisterFlag = True

            #5
            if operationCount < fifthDataRegisterAmount and operationType == "BONOS":
                fifthDataRegisterAmount = operationCount
                fifthDataRegisterName = name
                fifthDataRegisterIndex = i + 1

            #6
            if sixthDataRegisterFlag == False:
                sixthDataRegisterCost = operationCost
                sixthDataRegisterName = name
                sixthDataRegisterIndex = i + 1

            if operationCost < sixthDataRegisterCost:
                sixthDataRegisterCost = operationCost
                sixthDataRegisterName = name
                sixthDataRegisterIndex = i + 1
                sixthDataRegisterFlag == True

            #7
            if operationCount > seventhDataRegisterAmount:
                seventhDataRegisterAmount = operationCount
                seventhDataRegisterName = name
                seventhDataRegisterIndex = i + 1

            #8
            if operationType == "CEDEAR":
                eighthDataRegisterSum += operationCost

            #9
            if operationType == "MEP":
                ninthDataRegisterSum += operationCount

            print(f"El comprador N° {i + 1}")
            print(f"Su nombre es {name}")
            print(f"Compró {operationCount} de unidades de {operationType} por un total de ${operationCost}")
            print()

            message = f'''
            Es el comprador N° {i + 1}
            Su nombre es {name}
            "Compró {operationCount} de unidades de {operationType} por un total de ${operationCost}
            '''
            alert("Información de compra", message)

        #0
        if operationBONOSCounter < operationCEDEARCounter and operationBONOSCounter < operationMEPCounter:
            zeroDataRegisterType = "BONOS"
        elif operationCEDEARCounter < operationMEPCounter:
            zeroDataRegisterType = "CEDEAR"
        else:
            zeroDataRegisterType = "MEP"
        
        print(f"El instrumento menos operado es {zeroDataRegisterType}")

        #1
        if operationBONOSCounter > operationCEDEARCounter and operationBONOSCounter > operationMEPCounter:
            firstDataRegisterType = "BONOS"
        elif operationCEDEARCounter > operationMEPCounter:
            firstDataRegisterType = "CEDEAR"
        else:
            firstDataRegisterType = "MEP"

        print(f"El instrumento más operado es {firstDataRegisterType}")

        #2
        print(f"{secondDataRegisterAmount} usuarios compraron entre 50 y 200 unidades de MEP")

        #3
        print(f"{thirdDataRegisterAmount} usuarios no compraron unidades de CEDEAR")

        #4
        print(f"El primer usuario que compró BONOS o CEDEAR es {fourthDataRegisterName} con ${fourthDataRegisterCost} invertidos")

        #5
        print(f"El usuario que menos unidades de BONOS compró es {fifthDataRegisterName}, siendo el comprador N° {fifthDataRegisterIndex}")

        #6
        print(f"El usuario que menos invirtió es {sixthDataRegisterName}, siendo el comprador N°{sixthDataRegisterIndex}")

        #7
        print(f"El usuario que más cantidad de unidades compró es {seventhDataRegisterName}, siendo el comprador N°{seventhDataRegisterAmount}")

        #8
        if operationCEDEARCounter != 0:
            eighthDataRegisterAverage = eighthDataRegisterSum / operationCEDEARCounter

        print(f"El promedio invertido por operación en CEDEAR es de ${eighthDataRegisterAverage}")

        #9
        if operationMEPCounter != 0:
            ninthDataRegisterAverage = ninthDataRegisterSum / operationMEPCounter

        print(f"El promedio de unidades de MEP compradas es de {ninthDataRegisterAverage}")

    def btn_mostrar_informe_1(self):
        pass
        


    def btn_mostrar_informe_2(self):
        pass
        


    def btn_mostrar_informe_3(self):
        pass      


    def btn_mostrar_todos_on_click(self):
        pass

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
