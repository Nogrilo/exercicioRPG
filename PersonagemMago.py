from Personagem import Personagem
from ArmaduraCouro import ArmaduraCouro
from ArmaduraMalha import ArmaduraMalha

class PersonagemMago(Personagem):
    def __init__(self, nome, armadura):
        forca               = 10
        agilidade           = 10
        nome                = nome
        ataque              = 9
        defesa              = 5
        tipoDePersonagem    = "Mago"
        armadura            = armadura
        super().__init__(forca, agilidade, nome, ataque, defesa, tipoDePersonagem, armadura) 