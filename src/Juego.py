from src.Personaje import Personaje
from src.Tecnica import Tecnica
from random import randint
class Juego:

    def __init__(self, nombre):
        self.nombre=nombre
        self.p1= Personaje;
        self.t1= Tecnica;
        self.t2= Tecnica;
        self.p2= Personaje;
        self.personajes=[]
        self.jugador1=Personaje;
        self.jugador2=Personaje;
        self.hola=0;

    def carga(self):
        self.t1 = Tecnica("Gancho", 50, 0, 60, 85, 15)
        self.t2 = Tecnica("Rayo Solar", 0, 50, 20, 70, 35)
        self.p1 = Personaje("Moradin", 200, 30, 10, 20)
        self.p2= Personaje("Gandalf", 200, 30, 10, 20)
        self.p3 = Personaje("Tofol", 100000, 100000, 1000000, 1000000000)

        self.personajes.append(self.p1)
        self.personajes.append(self.p2)
        self.personajes.append(self.p3)
        self.p1.setTecinas(self.t1, self.t2)
        self.p2.setTecinas(self.t1, self.t2)
        self.p3.setTecinas(self.t1, self.t2)
        #self.p1.getTecnica()

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

    def listadoPersonajes(self):
        count=0
        print("Personajes:")
        print("-------------------------------------------------")
        for x in self.personajes:
            count = count + 1
            print(str(count) + " - " + str(x.getNombre()))
        print("-------------------------------------------------")

    def seleccion(self):

        j=input("-------------------------------------------------\n"+ "Adalid, por favor, seleccione un personaje: ")
        if j=="1":
            #Convertir a metodo.
            self.p1.descPersonaje()
            eleccion=input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
            if eleccion=="1":
                self.jugador1=self.p1
                print( "El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
                print("-------------------------------------------------")

            elif eleccion=="2":
                print("-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
                self.listadoPersonajes()
                self.seleccion()
        elif j=="2":
            self.p2.descPersonaje()
            eleccion = input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
            if eleccion == "1":
                self.jugador1 = self.p2
                print("El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
                print("-------------------------------------------------")
            elif eleccion == "2":
                print(
                    "-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
                self.listadoPersonajes()
                self.seleccion()

        elif j=="3":
            self.p3.descPersonaje()
            eleccion = input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
            if eleccion == "1":
                self.jugador1 = self.p3
                print("El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
                print("-------------------------------------------------")
            elif eleccion == "2":
                print(
                    "-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
                self.listadoPersonajes()
                self.seleccion()
        else :
            print ("Opcion incorrecta!")
            self.seleccion()

    def usarTecnica(self, jugador, enemigo):
        print("-------------------------------------------------")
        print("Tecnicas de: " + jugador.getNombre())
        jugador.getTecnica()
        print("3 - Pasar turno ")

        tec=input("Seleccione una tecnica: ")
        if tec=="1":
            #converit a metodo.
            if jugador.getTecnica1(0).getCosteEnergia()<=jugador.getEnergia():
                if (jugador.getTecnica1(0).getDanyoFisico()) > 0:
                    enemigo.recibirDanyoFisico(jugador.getTecnica1(0).getDanyoFisico())
                    jugador.restarEnergia(int(jugador.getTecnica1(0).getCosteEnergia()))
                elif (jugador.getTecnica1(0).getDanyoMagico()) > 0:
                    enemigo.recibirDanyoMagico(int(jugador.getTecnica1(0).getDanyoMagico()))
                    jugador.restarEnergia(jugador.getTecnica1(0).getCosteEnergia())
                print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() +  " es: " + str(enemigo.getVida()))
            else:
                print("EL jugador no tiene suficiente energia para realizar esta tecnica, seleccione otra")
                self.usarTecnica(jugador, enemigo)
        elif tec=="2":
            if jugador.getTecnica1(1).getCosteEnergia() <= jugador.getEnergia():
                if (jugador.getTecnica1(1).getDanyoFisico()) > 0:
                    enemigo.recibirDanyoFisico(jugador.getTecnica1(1).getDanyoFisico())
                    jugador.restarEnergia(int(jugador.getTecnica1(1).getCosteEnergia()))
                elif (jugador.getTecnica1(1).getDanyoMagico()) > 0:
                    enemigo.recibirDanyoMagico(int(jugador.getTecnica1(1).getDanyoMagico()))
                    jugador.restarEnergia(jugador.getTecnica1(1).getCosteEnergia())
                print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() + " es: " + str(
                    enemigo.getVida()))
            else:
                print("EL jugador no tiene suficiente energia para realizar esta tecnica, seleccione otra")
                self.usarTecnica(jugador, enemigo)
        elif tec=="3":
            print("Has pasado de turno")
        else:
            print("Opcion incorrecta, elija una tecnica valida")
            self.usarTecnica(jugador, enemigo)

    def eleccionBoss(self):
        r=randint(1,3)
        if r==1:
            self.jugador2=self.p1
        elif r==2:
            self.jugador2=self.p2
        elif r==3:
            self.jugador2=self.p3


    def bossAttacks(self):
        r = randint(1, 3)
        if self.hola==0:
            print("-------------------------------------------------\nTurno de: "+self.jugador2.getNombre()+ " enemigo, su energia es de: " + str(self.jugador2.getEnergia()) +  "\n-------------------------------------------------")

        if r==1:
            if self.jugador2.getTecnica1(0).getCosteEnergia() <= self.jugador2.getEnergia():
                if (self.jugador2.getTecnica1(0).getDanyoFisico()) > 0:
                    self.jugador1.recibirDanyoFisico(int(self.jugador2.getTecnica1(0).getDanyoFisico()))
                    print(self.jugador2.getNombre() +" va a usar "+ self.jugador2.getTecnica1(0).getNombre() )
                elif (self.jugador1.getTecnica1(0).getDanyoMagico()) > 0:
                    self.jugador1.recibirDanyoMagico(int(self.jugador2.getTecnica1(0).getDanyoMagico()))
                    print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(0).getNombre())
                self.hola=0
                self.jugador2.restarEnergia(int(self.jugador2.getTecnica1(0).getCosteEnergia()))
                print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() +  " es: " + str(self.jugador1.getVida()))
            else:
                self.hola= self.hola +1
                self.bossAttacks()
        elif r==2:
            if self.jugador2.getTecnica1(1).getCosteEnergia() <= self.jugador2.getEnergia():
                if (self.jugador2.getTecnica1(1).getDanyoFisico()) > 0:
                    self.jugador1.recibirDanyoFisico(int(self.jugador2.getTecnica1(1).getDanyoFisico()))
                    print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(1).getNombre())
                elif (self.jugador1.getTecnica1(1).getDanyoMagico()) > 0:
                    self.jugador1.recibirDanyoMagico(int(self.jugador2.getTecnica1(1).getDanyoMagico()))
                    print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(1).getNombre())
                self.hola = 0
                self.jugador2.restarEnergia(int(self.jugador2.getTecnica1(1).getCosteEnergia()))
                print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() + " es: " + str(self.jugador1.getVida()))
            else:
                self.hola= self.hola+1
                self.bossAttacks()
        elif r==3:
            self.hola = 0
            print("El enemigo paso de turno")
    def lucha(self):
        print("Que empiecen la arena")
        self.eleccionBoss()
        rondas=0;
        print("\n-------------------------------------------------\n"+self.jugador1.getNombre() + " VS " + self.jugador2.getNombre())
        while self.jugador1.getVida()>0 and self.jugador2.getVida()>0:
            rondas=rondas+1;
            print("-------------------------------------------------\nRonda: "+ str(rondas))
            print("Energia de " + str(self.jugador1.getNombre()) + ": " + str(self.jugador1.getEnergia()))
            self.usarTecnica(self.jugador1, self.jugador2)
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

j1 = Juego("LofotTheGathering")
j1.carga()
j1.juego()
j1.lucha()
