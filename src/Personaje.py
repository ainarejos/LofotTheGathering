from src import Tecnica

class Personaje:
    def __init__(self, nombre, vida, armadura, resist_Magica, energia):
        self.Nombre=nombre
        self.vida=vida
        self.Armadura=armadura
        self.Resist_Magica=resist_Magica
        self.Energia=energia;
        self.Tecnicas=[]

    def getNombre(self):
        return self.Nombre
    def getVida(self):
        return self.vida
    def getTecnica(self):
        cont=0
        for x in self.Tecnicas:
            cont=cont+1
            print(str(cont) + " - " + str(x.getNombre()))
    def getTecnica1(self, int):
        return self.Tecnicas[int]
    def getArmadura(self):
        return self.Armadura
    def getResist_Magica(self):
        return self.Resist_Magica
    def getEnergia(self):
        return self.Energia

    def setTecinas(self, Tecnica1, Tecnica2):
        self.Tecnicas.append(Tecnica1)
        self.Tecnicas.append(Tecnica2)

    def recibirDanyoFisico(self, int):
        if (int>self.Armadura):
            self.vida=self.vida-int+self.Armadura
        else:
            print("La armadura paro el ataque")
    def recibirDanyoMagico(self, int):
        if (int>self.Resist_Magica):
            self.vida = self.vida - int + self.Resist_Magica
        else:
            print(str(self.Nombre) + " resistió la tecnica")