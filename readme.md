Olá espero que todos estejam bem!

Esse algoritmo foi criado conforme a atividade proposta pelo Professor Tiago em Padrões de Projeto.
A atividade em si, seria criar um sistema com POO no padrão Bridge com o tema que quisse, ou sobre RPG.

Acabei obtando pelo tema do Professor.

"O padrão Bridge é um padrão de projeto estrutural que desacopla uma abstração de sua implementação, 
permitindo que ambas evoluam independentemente."

Analisando o código desenvolvido, esse padrão é aplicado em Personagem e Armadura.

Agora explicando o código, nos temos as seguintes classes:
- Armadura - classse Mãe
- ArmaduraCouro - classe Filha
- ArmaduraMahlha - classe Filha
- Main (que seria a interface)
- Personagem - classe Mãe
- PersonagemCavaleiro - classe Filha
- PersonagemMago - classe Filha

Para criarmos um personagem no software, precisamos passar seus parâmetros (Nome, Forca, defesa, dentre outros), e instanciar
armadura para ele. Não é possível criar um objeto da classe Personagem sem ter uma armadura!

Entretanto, temos diferentes classes no RPG, como podemos criar um objeto Cavaleiro, ou Mago por exemplo.
Com isso, ao invés de termos várias classes do tipo personagem, temos apenas a classe mãe "Personagem", juntamente com suas filhas, "PersonagemCavaleiro" e "PersonagemMago".

O mesmo acontece com Armadura. "ArmaduraCouro" e "ArmaduraMalha" são filhas da superclasse Armadura, que tem seus atributos já declarados dentro da classe.

Aplicando esse padrão de projeto, não vamos ter o problema de uma explosão de classes, como por exemplo "PersonagemCavaleiroComArmaduraDeMahlha", 
pois armadura é um atributo de personagem, e podemos definir o tipo dela, de quantas formas necessárias.

Então, para criarmos um personagem, no arquivo Main.py, digitamos o seguinte:

Nome do seu personagem/variável, a classe de RPG que ele será (sei que existe mais), e a armadura que ele usuará.
personagem = PersonagemCavaleiro("SeuPersonagem", SuaArmadura)
personagem.exibirDadosPersonagem()

Para concluir, acredito que consegui aplicar o método Bridge nesse exemplo :) 
