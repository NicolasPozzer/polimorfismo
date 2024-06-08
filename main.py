class Gato():    #Clase Gato
    def sonido(self):
        return "Miau"

class Perro():    #Clase Perro
    def sonido(self):
        return "Guau"


def hacer_sonido(animal):   #Funcion aparte
    print(animal.sonido())

perro = Perro()
gato = Gato()

#Llamado a funcion
hacer_sonido(gato)#Si cambio el parametro por "perro" solo
                  #  cambia el sonido al animal que pertenece
