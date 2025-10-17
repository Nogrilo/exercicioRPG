from ArmaduraCouro          import ArmaduraCouro
from ArmaduraMalha          import ArmaduraMalha
from Personagem             import Personagem
from PersonagemCavaleiro    import PersonagemCavaleiro
from PersonagemMago         import PersonagemMago

armaduraMalha = ArmaduraMalha()
armaduraCouro = ArmaduraCouro()

personagem01 = PersonagemCavaleiro("Nogrilo", armaduraCouro)
personagem01.exibirDadosPersonagem()

personagem02 = PersonagemMago("Teste", armaduraCouro)
personagem02.exibirDadosPersonagem()

