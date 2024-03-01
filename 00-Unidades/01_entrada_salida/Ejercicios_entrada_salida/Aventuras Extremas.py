import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
Ejercicio: Aventuras extremas
---
Enunciado:
En el parque de diversiones "Aventuras Extremas", un grupo de 10 amigos ha 
decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un
restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden 
crear un programa para calcular y dividir los gastos de manera equitativa. 
Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo (pedir por prompt)

Nombre del amigo, 
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
Cantidad de platos principales pedidos (debe ser al menos 1).
Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 1).


Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $3000.

El precio unitario de cada bebida es de $1000.


Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por print):

Informar cual fue el tipo de bebida más vendida.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas,
30% hamburguesas]
Informar la cantidad total de bebidas que fueron “Refresco”.
El promedio gastado en platos principales de tipo “Pizza” sobre el grupo de amigos en general.
El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”

bis 
cantidad de usuarios que pidieron mas de una bebida
cantidad de amigos que pidieron menos de un plato principal

el nombre del que compro mas bebidas
el nombre del que menos platos principales pidio 

el nombre de la persona que pidio mas pizzas
el promedio de bebidas por persona
el precio promedio de bebidas pagada por cada persona
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        mainCourseBasePrice = 3000
        drinkBasePrice = 1000

        counterSoda = 0
        accumulatorSoda = 0
        counterJuice = 0
        accumulatorJuice = 0
        counterWater = 0
        accumulatorWater = 0
        twoDrinkAmountCounter = 0
        maximumDrinkFlag = False

        counterPizza = 0
        accumulatorPizza = 0
        pizzaAveragePrice = 0
        pizzaPercentage = 0
        minimumBurgerFlag = False
        minimumMainCourseFlag = False
        maximumPizzaFlag = False
        counterBurger = 0
        accumulatorBurger = 0
        burgerPercentage = 0
        counterSalad = 0
        accumulatorSalad = 0
        saladPercentage = 0
        twoMainCourseAmountCounter = 0

        orderCounter = 0

        breakFlag = False

        finalMessage = ""

        while breakFlag == False:
            name = prompt("Input information", "Input friend's name")
            if name == None:
                name = "ERROR"
            elif name.isalpha() == False:
                name = "ERROR"

            while name == "ERROR":
                name = prompt("Input again", "Input friend's name")
                if name == None:
                    name = "ERROR"
                elif name.isalpha() == False:
                    name = "ERROR"


            mainCourse = prompt("Input information", "Input the main course (Burger - Pizza - Salad)")
            if mainCourse == None:
                mainCourse = "ERROR"
            elif mainCourse.isalpha() == False:
                mainCourse = "ERROR"

            while mainCourse != "Pizza" and mainCourse != "Burger" and mainCourse != "Salad":
                mainCourse = prompt("Input again", "Input the main course (Burger - Pizza - Salad)")
                if mainCourse == None:
                    mainCourse = "ERROR"
                elif mainCourse.isalpha() == False:
                    mainCourse = "ERROR"


            mainCourseAmount = prompt("Input information", "Input main course amount")
            if mainCourseAmount == None:
                mainCourseAmount = 0
            elif mainCourseAmount.isdigit() == True:
                mainCourseAmount = int(mainCourseAmount)
            else:
                mainCourseAmount = 0

            while mainCourseAmount < 1:
                mainCourseAmount = prompt("Input again", "Input main course amount")
                if mainCourseAmount == None:
                    mainCourseAmount = 0
                elif mainCourseAmount.isdigit() == True:
                    mainCourseAmount = int(mainCourseAmount)
                else:
                    mainCourseAmount = 0


            drink = prompt("Input information", "Input desired drink (Soda - Juice - Water)")
            if drink == None:
                drink = "ERROR"
            elif drink.isalpha() == False:
                drink = "ERROR"

            while drink != "Soda" and drink != "Juice" and drink != "Water":
                drink = prompt("Input again", "Input desired drink (Soda - Juice - Water)")
                if drink == None:
                    drink = "ERROR"
                elif drink.isalpha() == False:
                    drink = "ERROR"


            drinkAmount = prompt("Input information", "Input drinks amount")
            if drinkAmount == None:
                drinkAmount = 0
            elif drinkAmount.isdigit() == True:
                drinkAmount = int(drinkAmount)
            else:
                drinkAmount = 0

            while drinkAmount < 1:
                drinkAmount = prompt("Input again", "Input drinks amount")
                if drinkAmount == None:
                    drinkAmount = 0
                elif drinkAmount.isdigit() == True:
                    drinkAmount = int(drinkAmount)
                else:
                    drinkAmount = 0

            ############

            if question("Confirm", f"The friend's name is {name} \nThey ordered {mainCourseAmount} {mainCourse}s\nThey ordered {drinkAmount} {drink}s") == False:
                continue
            elif question("Confirm", "¿Do you want to continue?") == False:
                breakFlag = True
            print(f"The N°{orderCounter + 1} friend's name is {name} \nThey ordered {mainCourseAmount} {mainCourse}s\nThey ordered {drinkAmount} {drink}s\n")

            orderCounter += 1

            ###########
            match drink:
                case "Soda":
                    counterSoda += 1
                    accumulatorSoda += drinkAmount
                case "Juice":
                    counterJuice += 1
                    accumulatorJuice += drinkAmount
                case _:
                    counterWater += 1
                    accumulatorWater += drinkAmount

            match mainCourse:
                case "Pizza":
                    counterPizza += 1
                    accumulatorPizza += mainCourseAmount

                    if maximumPizzaFlag == False:
                        maximumPizzaAmount = mainCourseAmount
                        maximumPizzaName = name
                        maximumPizzaFlag = True
                    elif mainCourseAmount < maximumPizzaAmount:
                        maximumPizzaAmount = mainCourseAmount
                        maximumPizzaName = name
                case "Burger":
                    counterBurger += 1
                    accumulatorBurger += mainCourseAmount

                    
                    if minimumBurgerFlag == False:
                        minimumBurgerAmount = mainCourseAmount
                        minimumBurgerName = name
                        minimumBurgerFlag = True
                    elif mainCourseAmount < minimumBurgerAmount:
                        minimumBurgerAmount = mainCourseAmount
                        minimumBurgerName = name
                case _:
                    counterSalad += 1
                    accumulatorSalad += mainCourseAmount

            if drinkAmount > 1:
                twoDrinkAmountCounter += 1


            if maximumDrinkFlag == False:
                maximumDrinkAmount = mainCourseAmount
                maximumDrinkName = name
                maximumDrinkFlag = True
            elif mainCourseAmount > maximumDrinkAmount:
                maximumDrinkAmount = mainCourseAmount
                maximumDrinkName = name

            if mainCourseAmount < 2:
                twoMainCourseAmountCounter += 1
            
            if minimumMainCourseFlag == False:
                minimumMainCourseAmount = mainCourseAmount
                minimumMainCourseName = name
                minimumMainCourseFlag = True
            elif mainCourseAmount < minimumMainCourseAmount:
                minimumMainCourseAmount = mainCourseAmount
                minimumMainCourseName = name

            

        if accumulatorSoda > accumulatorJuice and accumulatorSoda > accumulatorWater:
            mostDrinksType = "Soda"
            mostDrinksAmount = accumulatorSoda
        elif accumulatorJuice > accumulatorWater:
            mostDrinksType = "Juice"
            mostDrinksAmount = accumulatorJuice
        else:
            mostDrinksType = "Water"
            mostDrinksAmount = accumulatorWater

        mainCoursesTotal = accumulatorPizza + accumulatorBurger + accumulatorSalad

        drinksTotal = accumulatorJuice + accumulatorSoda + accumulatorWater
        drinksAverage = drinksTotal / orderCounter
        drinksAverage = round(drinksAverage, 1)
        drinksAveragePrice = drinkBasePrice * drinksAverage

        if accumulatorPizza != 0:
            pizzaPercentage = (accumulatorPizza / mainCoursesTotal) * 100
            pizzaPercentage = round(pizzaPercentage, 1)
        if accumulatorBurger != 0:
            burgerPercentage = (accumulatorBurger / mainCoursesTotal) * 100
            burgerPercentage = round(burgerPercentage, 1)
        if accumulatorSalad != 0:
            saladPercentage = (accumulatorSalad / mainCoursesTotal) * 100
            saladPercentage = round(saladPercentage, 1)

        if counterPizza != 0:
            pizzaAverage = accumulatorPizza / orderCounter
            pizzaAveragePrice = pizzaAverage * mainCourseBasePrice

        if accumulatorJuice != 0 or accumulatorSoda != 0 or accumulatorWater != 0:
            finalMessage += f"The drink that was sold the most is {mostDrinksType}, with {mostDrinksAmount} units.\n"
            finalMessage += f"{pizzaPercentage}% of the courses were Pizza, {burgerPercentage}% were Burgers, {saladPercentage} were Salads.\n"
            finalMessage += f"{accumulatorSoda} drinks were Soda.\n"
        else:
            finalMessage += f"No drinks or courses were bought.\n"

        finalMessage += f"A total of ${pizzaAveragePrice} in pizzas were spent per person in average.\n"
        if minimumBurgerFlag == True:
            finalMessage += f"{minimumBurgerName} ordered the least burgers, with {minimumBurgerAmount} units.\n"
        else:
            finalMessage += f"No one ordered burgers\n"
        finalMessage += f"{twoDrinkAmountCounter} people ordered more than 1 drink\n"
        finalMessage += f"{twoMainCourseAmountCounter} people ordered less than 2 main courses\n"
        finalMessage += f"{maximumDrinkName} ordered de most drinks, with {maximumDrinkAmount} units\n"
        finalMessage += f"{minimumMainCourseName} ordered the least main courses, with {minimumMainCourseAmount} units\n"
        if maximumPizzaFlag == True:
            finalMessage += f"{maximumPizzaName} ordered the most pizzas, with {maximumPizzaAmount} units\n"
        else:
            finalMessage += f"No one ordered pizzas\n"
        finalMessage += f"{drinksAverage} drinks were ordered per person\n"
        finalMessage += f"A total of ${drinksAveragePrice} in drinks were spent per person on average"
            
        print(finalMessage)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
