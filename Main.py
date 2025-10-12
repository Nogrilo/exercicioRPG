from ArmaduraCouro  import ArmaduraCouro
from ArmaduraMalha  import ArmaduraMalha
from Personagem     import Personagem

def definirPersonagem():
    armaduraFraca   = ArmaduraCouro()
    personagem01    = Personagem(10, 5, "Piteus", 10, 4, "Cavaleiro", armaduraFraca)
    personagem01.exibirDadosPersonagem()

if __name__ == "__main__":
    definirPersonagem()