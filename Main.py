from ArmaduraCouro          import ArmaduraCouro
from ArmaduraMalha          import ArmaduraMalha
from Personagem             import Personagem
from PersonagemCavaleiro    import PersonagemCavaleiro

armaduraMalha = ArmaduraMalha()
armaduraCouro = ArmaduraCouro()

personagem01 = PersonagemCavaleiro("Nogrilo", armaduraCouro)
personagem01.exibirDadosPersonagem()

