class Car:
    def __init__(self, mark, year, model, motor, km, cost):
        self.mark = mark
        self.year = year
        self.model = model
        self.motor = motor
        self.km = km
        self.cost = cost


Chevrolet = Car("Chevrolet", "2018", "Sail", "109 hp", "0 km", "45,000.00")
Toyota = Car("Toyota", "2018", "Fortuner", "163 hp", "0 km", "34,500.00")
Honda = Car("Honda", "2016", "HR-V", "141 hp", "100 km", "20,104.00")
Nissan = Car("Nissan", "2017", "SUV", "118 hp", "50 km", "26,700.00")


class Buy:
    def buying(self):
        print "Que marca de auto le gustaria adquirir"
        print ("\t1 - Chevrolet")
        print ("\t2 - Toyota")
        print ("\t3 - Honda")
        print ("\t4 - Nissan")
        print ("\t5 - Regresar al Menu principal")


class Pay():
    pass


class Menu():

    while True:
        Buy().buying()
        options = input("Ingrese el numero de la opcion que desee")

        if options == 1:
            print "Lista de Autos disponibles Chevrolet"
            print Chevrolet.mark, " Modelo: ", Chevrolet.model, " Anio: ", Chevrolet.year, " Motor: ", Chevrolet.motor, " Kilometraje: ", Chevrolet.km, " Precio: ", Chevrolet.cost
            pay = raw_input("desea comprar este auto?")
            if pay == "si":
                print "Compra exitosa"
                break
            elif pay == "no":
                print "Regresando al menu de seleccion"
        elif options == 2:
            print "Lista de Autos disponibles Toyota"
            print Toyota.mark, " Modelo: ", Toyota.model, " Anio: ", Toyota.year, " Motor: ", Toyota.motor, " Kilometraje: ", Toyota.km, " Precio: ", Toyota.cost
            print "desea comprar este auto?"
            pay = raw_input()
            if pay == "si":
                print "Compra exitosa"
                break
            elif pay == "no":
                print "Regresando al menu de seleccion"
        elif options == 3:
            print "Lista de Autos disponibles Honda"
            print Honda.mark, " Modelo: ", Honda.model, " Anio: ", Honda.year, " Motor: ", Honda.motor, " Kilometraje: ", Honda.km, " Precio: ", Honda.cost
            print "desea comprar este auto?"
            pay = raw_input()
            if pay == "si":
                print "Compra exitosa"
                break
            elif pay == "no":
                print "Regresando al menu de seleccion"
        elif options == 4:
            print "Lista de Autos disponibles Nissan"
            print Nissan.mark, " Modelo: ", Nissan.model, " Anio: ", Nissan.year, " Motor: ", Nissan.motor, " Kilometraje: ", Nissan.km, " Precio: ", Nissan.cost
            print "desea comprar este auto?"
            pay = raw_input()
            if pay == "si":
                print "Compra exitosa"
                break
            elif pay == "no":
                print "Regresando al menu de seleccion"
        elif options == 5:
            break
        else:
            print "Valor Incorrecto"


Menu()
