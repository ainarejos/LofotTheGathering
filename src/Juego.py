from src.Personaje import Personaje
from src.Tecnica import Tecnica
from random import randint
class Juego:

    def __init__(self, nombre):
        #Atributos.
        self.nombre=nombre

        #Personajes, p=Aliados, e=Enemigos.
        self.p1 = Personaje
        self.p2 = Personaje
        self.p3 = Personaje
        self.p4 = Personaje
        self.p5 = Personaje
        self.p6 = Personaje

        self.e1 = Personaje
        self.e2 = Personaje
        self.e3 = Personaje
        self.e4 = Personaje
        self.e5 = Personaje
        self.e6 = Personaje

        #Arraylist de personajes.
        self.personajes = []

        #Tecnicas
        self.t1 = Tecnica
        self.t2 = Tecnica
        self.t3 = Tecnica
        self.t4 = Tecnica
        self.t5 = Tecnica
        self.t6 = Tecnica

        #Jugadores
        self.jugador1=Personaje
        self.jugador2=Personaje

        #Contador.
        self.contador=0

    #Metodo en el que se instancian todos los objetos necesarios para la ejecuión del juego.
    def carga(self):
        #Personajes
        #Aliados
        self.p1 = Personaje("Moradin", 200, 30, 10, 20)
        self.p2 = Personaje("Gandalf", 180, 10, 40, 20)
        self.p3 = Personaje("Torvald", 210, 15, 35, 20)
        self.p4 = Personaje("Vanir", 170, 50, 15, 20)
        self.p5 = Personaje("Lariat", 160, 40, 30, 35)
        self.p6 = Personaje("Diluc", 205, 35, 10, 20)

        #Enemigos
        self.e1 = Personaje("Moradin", 200, 30, 10, 20)
        self.e2 = Personaje("Gandalf", 200, 30, 10, 20)
        self.e3 = Personaje("Torvald", 210, 15, 35, 20)
        self.e4 = Personaje("Vanir", 170, 50, 15, 20)
        self.e5 = Personaje("Lariat", 160, 40, 30, 35)
        self.e6 = Personaje("Diluc", 205, 35, 10, 20)

        #Se añaden los personajes aliados al arraylist de personajes.
        self.personajes.append(self.p1)
        self.personajes.append(self.p2)
        self.personajes.append(self.p3)
        self.personajes.append(self.p4)
        self.personajes.append(self.p5)
        self.personajes.append(self.p6)

        #Tecnicas.
        self.t1 = Tecnica("Gancho", 50, 0, 15)
        self.t2 = Tecnica("Rayo Solar", 0, 65, 35)
        self.t3 = Tecnica("Apuñalada", 30, 0, 10)
        self.t4 = Tecnica("Bola de fuego", 0, 45, 35 )
        self.t5 = Tecnica("Estoque", 80, 0, 45)
        self.t6 = Tecnica("Marca oscura", 90, 0, 55)


        #Se añaden las tecnicas a cada personaje.
        self.p1.setTecinas(self.t1, self.t2)
        self.p2.setTecinas(self.t2, self.t4)
        self.p3.setTecinas(self.t1, self.t6)
        self.p4.setTecinas(self.t4, self.t3)
        self.p5.setTecinas(self.t3, self.t5)
        self.p6.setTecinas(self.t5, self.t1)

        self.e1.setTecinas(self.t1, self.t2)
        self.e2.setTecinas(self.t2, self.t4)
        self.e3.setTecinas(self.t6, self.t2)
        self.e4.setTecinas(self.t4, self.t3)
        self.e5.setTecinas(self.t3, self.t5)
        self.e6.setTecinas(self.t5, self.t1)

    #Metodo que se ejecuta al inicio del juego, este muestra el nombre del juego y llama a otros metodos.
    def juego(self):
        print("-------------------------------------------------\n _            __      _     _______ _\n"+
              "| |          / _|    | |   |__   __| |\n"+
"| |     ___ | |_ ___ | |_     | |  | |__   ___\n"+
"| |    / _ \|  _/ _ \| __|    | |  | '_ \ / _ \ \n"+
"| |___| (_) | || (_) | |_     | |  | | | |  __/ \n"+
"|______\___/|_| \___/ \__|    |_|  |_| |_|\___|\n" +
  " _____        _   _               _ \n"+
 "/  ____|     | | | |             (_)\n"+
"| |  __  __ _| |_| |__   ___ _ __ _ _ __   __ _ \n"+
"| | |_ |/ _` | __| '_ \ / _ \ '__| | '_ \ / _` |\n"+
"| |__| | (_| | |_| | | |  __/ |  | | | | | (_| |\n"+
"\_____|\__,_|\__|_| |_|\___| _|  |_|_| |_|\__, |\n"+
                                           "\t\t\t\t\t\t\t\t\t\t   __/ |\n"+
                                          "\t\t\t\t\t\t\t\t\t\t  |___/"+"\n-------------------------------------------------" )
        self.listadoPersonajes()
        self.seleccion()

    #Este metodo muestra la lista de personajes.
    def listadoPersonajes(self):
        count=0
        print("Personajes:")
        print("-------------------------------------------------")
        for x in self.personajes:
            count = count + 1
            print(str(count) + " - " + str(x.getNombre()))
        print("-------------------------------------------------")

    #Este metodo pide al usuario que elija uno de los personajes.
    def seleccion(self):
        j=input("-------------------------------------------------\n"+ "Adalid, por favor, seleccione un personaje: ")
        if j=="1":
            self.eleccion(self.p1)
        elif j=="2":
            self.eleccion(self.p2)
        elif j=="3":
            self.eleccion(self.p3)
        elif j=="4":
            self.eleccion(self.p4)
        elif j=="5":
            self.eleccion(self.p5)
        elif j=="6":
            self.eleccion(self.p6)
        else :
            print ("Opcion incorrecta!")
            self.seleccion()

    #Este metodo complementa al anterior, pide confirmacion al usuario por si este desea elegir finalmente otro.
    def eleccion(self, personaje):
        personaje.descPersonaje()
        eleccion = input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
        if eleccion == "1":
            self.jugador1 = personaje
            print("El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
            print("-------------------------------------------------")
        elif eleccion == "2":
            print(
                "-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
            self.listadoPersonajes()
            self.seleccion()
        else:
            print("Opcion incorrecta!")
            self.eleccion(personaje)

    #Este metodo pide al usuario que elija la tecnica que desea utilizar.
    def seleccionarTecnica(self, jugador, enemigo):
        print("-------------------------------------------------")
        print("Tecnicas de: " + jugador.getNombre())
        jugador.getTecnica()
        print("3 - Pasar turno ")

        tec=input("Seleccione una tecnica: ")
        if tec=="1":
            self.dañoTecnica(0, jugador, enemigo)
        elif tec=="2":
            self.dañoTecnica(1, jugador, enemigo)
        elif tec=="3":
            print("Has pasado de turno")
        else:
            print("Opcion incorrecta, elija una tecnica valida")
            self.seleccionarTecnica(jugador, enemigo)

    #Este metodo resta al enemigo el daño de la tecnica seleccionada por el usuario,
    # además en este metodo le resta la energia que necesita la tecnica
    def dañoTecnica(self, tecnica, jugador, enemigo):
        if jugador.getTecnica1(tecnica).getCosteEnergia() <= jugador.getEnergia():
            if (jugador.getTecnica1(tecnica).getDanyoFisico()) > 0:
                enemigo.recibirDanyoFisico(jugador.getTecnica1(tecnica).getDanyoFisico())
                self.jugador1.restarEnergia(int(jugador.getTecnica1(tecnica).getCosteEnergia()))
            elif (jugador.getTecnica1(1).getDanyoMagico()) > 0:
                enemigo.recibirDanyoMagico(int(jugador.getTecnica1(tecnica).getDanyoMagico()))
                self.jugador1.restarEnergia(jugador.getTecnica1(tecnica).getCosteEnergia())
            print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() + " es: " + str(
                enemigo.getVida()))
        else:
            print("EL jugador no tiene suficiente energia para realizar esta tecnica, seleccione otra")
            self.seleccionarTecnica(jugador, enemigo)

    #Este metodo utiliza un numero aleatorio entre el 1 y el 3 para la eleccion del personaje enemigo.
    def eleccionBoss(self):
        r=randint(1,3)
        if r==1:
            self.jugador2=self.e1
        elif r==2:
            self.jugador2=self.e2
        elif r==3:
            self.jugador2=self.e3
        elif r==4:
            self.jugador2=self.e4
        elif r==5:
            self.jugador2=self.e5
        elif r==6:
            self.jugador2=self.e6


    #Este metodo utiliza un numero aleatorio de ntre el 1 y el 3 para elegir la accion que realizara el enemigo.
    def bossAttacks(self):
        r = randint(1, 3)
        if self.contador==0:
            print("-------------------------------------------------\nTurno de: "+self.jugador2.getNombre()+ " enemigo, su energia es de: " + str(self.jugador2.getEnergia()) +  "\n-------------------------------------------------")
        if r==1:
            self.dañoTecnicaboss(0)
        elif r==2:
            self.dañoTecnicaboss(1)
        elif r==3:
            self.contador = 0
            print("El enemigo paso de turno")

    # Este metodo resta al usuario el daño de la tecnica que ha tocado en el metodo bossAttaks,
    # además en este metodo le resta la energia que necesita la tecnica
    def dañoTecnicaboss(self, tecnica):
        if self.jugador2.getTecnica1(tecnica).getCosteEnergia() <= self.jugador2.getEnergia():
            if (self.jugador2.getTecnica1(tecnica).getDanyoFisico()) > 0:
                print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(0).getNombre())
                self.jugador1.recibirDanyoFisico(int(self.jugador2.getTecnica1(tecnica).getDanyoFisico()))
            elif (self.jugador2.getTecnica1(tecnica).getDanyoMagico()) > 0:
                print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(tecnica).getNombre())
                self.jugador1.recibirDanyoMagico(int(self.jugador2.getTecnica1(tecnica).getDanyoMagico()))
            self.contador = 0
            self.jugador2.restarEnergia(int(self.jugador2.getTecnica1(tecnica).getCosteEnergia()))
            print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() + " es: " + str(
                self.jugador1.getVida()))
        else:
            self.contador = self.contador + 1
            self.bossAttacks()


    #Este metodo consta de un bucle en el que van atacando primero el jugador y despues el enemigo,
    #este bucle acabará cuando uno de los dos pierda toda su vida
    def lucha(self):
        print("Que empiecen la arena")
        self.eleccionBoss()
        rondas=0;
        print("\n-------------------------------------------------\n"+self.jugador1.getNombre() + " VS " + self.jugador2.getNombre())
        while self.jugador1.getVida()>0 and self.jugador2.getVida()>0:
            rondas=rondas+1;
            print("-------------------------------------------------\nRonda: "+ str(rondas))
            print("Energia de " + str(self.jugador1.getNombre()) + ": " + str(self.jugador1.getEnergia()))
            self.seleccionarTecnica(self.jugador1, self.jugador2)
            self.jugador1.sumarEnergia()

            if (self.jugador2.getVida()>0):
                self.bossAttacks()
                self.jugador2.sumarEnergia()

        if (self.jugador1.getVida()<=0):
            print("\n-------------------------")
            print("Ha ganado:" + str(self.jugador2.getNombre()))
        else:
            print("\n-------------------------")
            print("Ha ganado:" + str(self.jugador1.getNombre()))

#Ejecución
j1 = Juego("LofotTheGathering")
j1.carga()
j1.juego()
j1.lucha()
