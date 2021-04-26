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
        self.personajes.append(self.p1)
        self.personajes.append(self.p2)
        self.p1.setTecinas(self.t1, self.t2)
        self.p2.setTecinas(self.t1, self.t2)
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
        print("El jugador 1 ha seleccionado a: " + str(self.jugador1.getNombre()))
        print("-------------------------------------------------")
        j2 = input("Jugador 2, seleccione un personaje: ")
        if j2 == "1":
            self.jugador2 = self.p1
        elif j2 == "2":
            self.jugador2 = self.p2
        print("El jugador 2 ha seleccionado a: " + str(self.jugador2.getNombre()))

    def usarTecnica(self, jugador, enemigo):
        print("----------------------")
        print("Tecnicas de: " + jugador.getNombre())
        print(jugador.getTecnica())
        tec=input("Seleccione una tecnica: ")
        if tec=="1":
            enemigo.recibirDanyo(int(jugador.getTecnica1(0).getDanyoFisico()))
            print(enemigo.getVida())




    def lucha(self):
        print("Que empiecen los Juegos del Hambre")
        rondas=0;
        while self.jugador1.getVida()>0 and self.jugador2.getVida()>0:
            rondas=rondas+1;
            print("Ronda: " + str(rondas))
            self.usarTecnica(self.jugador1, self.jugador2)
            print("patata")
            break



j1 = Juego("LofotTheGathering")
j1.carga()
j1.seleccion()
j1.lucha()
