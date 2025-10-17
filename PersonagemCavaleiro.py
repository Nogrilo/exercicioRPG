from Personagem import Personagem
from ArmaduraCouro import ArmaduraCouro
from ArmaduraMalha import ArmaduraMalha

class PersonagemCavaleiro(Personagem):
    def __init__(self, nome, armadura):
        forca               = 10
        agilidade           = 5
        nome                = nome
        ataque              = 10
        defesa              = 10
        tipoDePersonagem    = "Cavaleiro"
        armadura            = armadura
        super().__init__(forca, agilidade, nome, ataque, defesa, tipoDePersonagem, armadura) 