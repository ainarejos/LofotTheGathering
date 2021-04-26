from src.Personaje import Personaje
from src.Tecnica import Tecnica
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

    def carga(self):
        self.t1 = Tecnica("Gancho", 15, 0, 60, 85, 20)
        self.t2 = Tecnica("Rayo Solar", 0, 30, 20, 70, 35)
        self.p1 = Personaje("Moradin", 80, 30, 10, 100)
        self.p2= Personaje("Gandalf", 80, 30, 10, 100)
        self.p3 = Personaje("Tofol", 100000, 100000, 1000000, 1000000000)

        self.personajes.append(self.p1)
        self.personajes.append(self.p2)
        self.personajes.append(self.p3)
        self.p1.setTecinas(self.t1, self.t2)
        self.p2.setTecinas(self.t1, self.t2)
        self.p3.setTecinas(self.t1, self.t2)
        #self.p1.getTecnica()

    def seleccion(self):
        print("Lofot The Gathering\n-------------------" )
        count=0
        print("Personajes:")
        print("------------")
        for x in self.personajes:
            count = count + 1
            print(str(count) + " - " + str(x.getNombre()))
        print("------------")
        j1=input("Jugador 1, seleccione un personaje: ")
        if j1=="1":
            self.jugador1=self.p1
        elif j1=="2":
            self.jugador1=self.p2
        elif j1=="3":
            self.jugador1=self.p3
        print("El jugador 1 ha seleccionado a: " + str(self.jugador1.getNombre()))
        print("-------------------------------------------------")
        j2 = input("Jugador 2, seleccione un personaje: ")
        if j2 == "1":
            self.jugador2 = self.p1
        elif j2 == "2":
            self.jugador2 = self.p2
        elif j2=="3":
            self.jugador2=self.p3
        print("El jugador 2 ha seleccionado a: " + str(self.jugador2.getNombre()))

    def usarTecnica(self, jugador, enemigo):
        print("----------------------")
        print("Tecnicas de: " + jugador.getNombre())
        print(jugador.getTecnica())
        tec=input("Seleccione una tecnica: ")
        if tec=="1":
            if (jugador.getTecnica1(0).getDanyoFisico()) > 0:
                enemigo.recibirDanyoFisico(int(jugador.getTecnica1(0).getDanyoFisico()))
            elif (jugador.getTecnica1(0).getDanyoMagico()) > 0:
                enemigo.recibirDanyoMagico(int(jugador.getTecnica1(0).getDanyoMagico()))
            print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() +  " es: " + str(enemigo.getVida()))

        elif tec=="2":
            if (jugador.getTecnica1(1).getDanyoFisico()) > 0:
                enemigo.recibirDanyoFisico(int(jugador.getTecnica1(1).getDanyoFisico()))
            elif (jugador.getTecnica1(1).getDanyoMagico()) > 0:
                enemigo.recibirDanyoMagico(int(jugador.getTecnica1(1).getDanyoMagico()))
            print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() +  " es: " + str(enemigo.getVida()))




    def lucha(self):
        print("Que empiecen los Juegos del Hambre")
        rondas=0;
        while self.jugador1.getVida()>0 and self.jugador2.getVida()>0:
            rondas=rondas+1;
            print("------------")
            print("Ronda: " + str(rondas))
            print("-------------")
            self.usarTecnica(self.jugador1, self.jugador2)
            print("")

            if (self.jugador2.getVida()>0):
                self.usarTecnica(self.jugador2, self.jugador1)


j1 = Juego("LofotTheGathering")
j1.carga()
j1.seleccion()
j1.lucha()
