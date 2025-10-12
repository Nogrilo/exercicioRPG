from abc import ABC, abstractmethod

class Armadura(ABC):
    def __init__ (self, tipoArmadura, durabilidadeArmadura, bonusDefesaArmadura):
        self.tipoArmadura           = tipoArmadura
        self.durabilidadeArmadra    = durabilidadeArmadura
        self.bonusDefesaArmadura    = bonusDefesaArmadura