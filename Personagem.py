from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, forca, agilidade, nome, ataque, defesa, tipoDePersonagem, armadura):
        self.forca               = forca
        self.agilidade           = agilidade
        self.nome                = nome
        self.ataque              = ataque
        self.defesa              = defesa
        self.tipoDePersonagem    = tipoDePersonagem
        self.armadura            = armadura

    def exibirDadosPersonagem(self):
        print("Personagem: ", self.nome)
        print("Forca: ", self.forca)
        print("Agilidade: ", self.agilidade)
        print("Ataque: ", self.ataque)
        print("Defesa: ", self.defesa)
        print("Classe: ", self.tipoDePersonagem)
        print("Armadura: ", self.armadura.tipoArmadura)