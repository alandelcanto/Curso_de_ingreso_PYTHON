import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alan
apellido: del Canto
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        name = prompt("Nombre", "Ingrese el nombre del candidato")

        age = prompt("Edad", "Ingrese la edad del ingresantes")
        age = int(age)

        voteCount = prompt("Votos", "Ingrese la cantidad de votos")
        voteCount = int(voteCount)

        maximumVoteCount = voteCount
        minimumVoteCount = voteCount

        voteTotalCount = 0

        ageCounter = 0
        ageSum = 0

        minimumVoteAge = 0
        minimumVoteName = 0

        maximumVoteName = 0

        while True:
            name = prompt("Nombre", "Ingrese el nombre del candidato")
            if name == None:
                break

            while age < 25:
                age = prompt("Edad", "Ingrese la edad del candidato")
                age = int(age)
            if age == None:
                break
            

            while voteCount < 0: 
                voteCount = prompt("Votos", "Ingrese la cantidad de votos del candidato")
                voteCount = int(voteCount)
            if voteCount == None:
                break
            

            if voteCount > maximumVoteCount:
                maximumVoteCount = voteCount
                maximumVoteName = name

            elif voteCount < minimumVoteCount:
                minimumVoteCount = voteCount
                minimumVoteName = name
                minimumVoteAge = age

            ageCounter += 1
            ageSum += age

            voteTotalCount += voteCount

        ageAverage = ageSum / ageCounter

        message = f'''
        El candidato con más votos es {maximumVoteName} con {maximumVoteCount} votos.
        El candidato menos votado es {minimumVoteName}, y tiene {minimumVoteAge} años.
        El promedio de edad de los candidatos es de {ageAverage} años.
        La cantidad total de votos emitidos es de {voteTotalCount} votos.
        '''

        alert ("Información de elecciones", message)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
