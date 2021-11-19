#Essa função tem o papel de filtro de idade, já que o jogo pode ter conteúdo sensível para certo público,
#pois o jogo é de terror.
def main ():
    classificacao = int(input("Digite aqui sua idade caso queira jogar: "))
    if classificacao >= 18:
        print("Você poderá jogar. Espero que tenha um ótimo jogo! ")
        instrucoes()
    elif classificacao < 18:
        print("Infelizmente você não poderá jogar devido a sua idade. ")
        main()
    else:
        print("digite um número válido.")
#Aqui você encontrará as instruções para poder jogar.
def instrucoes():
    print("Este é um jogo onde suas decisões terão um impacto direto nos personagens."
    "\nVocê deverá escolher entre as opções apresentadas para realizar as ações. Tenha um ótimo jogo! ")

    jogar = float(input("Se quiser jogar, digite 1. Caso não queira, digite 2: "))
    if jogar == 1:
        espaco= print("\n")
        intro()      
    elif jogar == 2:
        print("Até mais")
        main()
    else:
        print("Digite um número válido.")
#Esta função serve para ambientar o jogador. É uma breve história com a opção de personagem logo em seguida.
def intro():
    print("Você e seus amigos (Um grupo de 5 pessoas ao todo) estão realizando uma viagem de férias."
     "\nHá anos vocês tentavam organizar uma viagem, mas nunca conseguiam. Agora vocês estão viajando "
     "\npara um lugar que fica dentro de uma remota floresta, em meio as montanhas, cuja área é "
     "\nrodeada de lendas, principalmente envolvendo espíritos e assombrações. Vocês não ligam para os rumores, "
     "\nmas focam na tranquilidade e no bom tempo que poderão desfrutar juntos. "
     "\nApós uma longa viagem passando por estradas ruins e desfiladeiros, vocês conseguem ver a cabana. "
     "\nEm frente a cabana existe um espaço com vários bancos e uma fogueira para um momento de descontração. Da " 
     "\nfogueira para a cabana dá uma distância de uns 15 metros. "
     "\nDo lado esquerdo é possível visualizar vários arbustos, mas um pouco a frente está um desfiladeiro com mais "
     "\nde 30 metros de altura. Do lado direito existe uma trilha que leva floresta adentro. Quando a noite cai, "
     "\nambos os lugares são de baixa visualização.")
    escolha= int(input("Você deverá selecionar '1', '2' ou '3' para escolher o personagem com quem jogará: "))
    if escolha == 1:
        personagem_Sam()
    elif escolha == 2:
        personagem_Laurie()
    elif escolha == 3:
        personagem_Daniel()
    else:
        print("Escolha uma opção válida.")    
#Aqui começa a história com o personagem Sam. Breve introdução e escolhas.
def personagem_Sam():
    print("Você escolheu o Sam. Sam é um rapaz extrovertido, leal aos amigos e que trabalha atualmente no ramo "
     "\besportivo, onde tem investido em produtos para alta performance. Ele jogava no time da faculdade. ")
    print("\n")
    print("Já anoiteceu e você e seus amigos resolveram ir para perto da fogueira. Já ao lado da fogueira, vocês "
    "\ncomeçam a conversar sobre as lendas locais. Conta-se que há centenas de anos houve um massacre causado devido "
    "\numa guerra travada ali. Conforme a lenda vai sendo contada, o clima entre todos toma uma forma apreensiva. "
    "\nJessica te chama e pede para ir até a cozinha para pegar mais marshmallow e mais algumas bebidas. Você vai. "
    "\nA cabana é feita de madeira, então ouve-se ruídos em todos os cômodos. Você chega na cozinha que fica na "
    "\nparte de trás da casa, você abre a geladeira e pega as cervejas. Logo em seguida você vai ao armário "
    "\ne pega o marshmallow. Assim que você pega e começa a fechar o armário, através de uma pequena janela entre a "
    "\na geladeira e o armário (onde fica a pia) você vê um vulto do lado de fora e ouve um barulho vindo da "
    "\nmesma direção. Um barulho alto, mas devido a distância sua e do grupo, só você ouve. Você abre a porta "
    "\ndos fundos para tentar ver melhor, mas fica em dúvida do que fazer. Qual será sua escolha? ")
    print("\n")
    decisao = int(input("Se você decide investigar o barulho, digite 1. Se decide voltar ao grupo, 2: "))
    print("\n)")
    while decisao == 1:
        print("Você decide investigar o barulho e sai atrás do vulto")
        situacao_1_Sam()
    while decisao == 2:
        print("você sente a necessidade de averiguar o que está acontecendo para a sua segurança e a de seus "
        "\namigos")
        print("\n")
        break
    situacao_1_Sam()
#Situações que podem ocorrer com o personagem Sam.
def situacao_1_Sam():
    print("Você decidiu sair para investigar o vulto e o barulho. A luz da casa ilumina só um pouco, mas não até "
    "\nonde você está indo. Você já se afastou um pouco da casa em linha reta e o barulho começou a ficar mais intenso, "
    "\nchegando a lhe causar calafrios. Você olha para todos os lados mas não vê nada. Ao contrário, acaba  "
    "\ntropeçando em uma pedra e caindo. Você se levanta e sente que tem alguém lhe observando fixamente. Você "
    "\nlevanta, olha para frente e não vê nada, para o lado esquerdo idem. Mas quando olha para o direito, vê uma figura "
    "\ntotalmente aterrorizante. Com o cabelo cobrindo uma parte do rosto, cicatrizes e cortes na outra parte "
    "\ne com um olhar tão penetrante que a sensação é como se fosse de encontro à sua alma. "
    "\nO que você faz? ")
    print("\n")
    escolha = int(input("Se você decide correr para o lado oposto da figura, digite 1. Caso tente acertar "
    "\na figura com uma pedra que está perto de você, digite 2: "))
    print("\n")
    if escolha == 1:
        print("Com a criatura olhando nos seus olhos de uma forma que parecia que você tinha perdido a alma, "
        "\nvocê não pensa duas vezes e começa a correr para o lado oposto. Você correr sem olhar para trás "
        "\nenquanto ouve aquele horrendo barulho de outrora. Mas infelizmente por estar totalmente escuro e "
        "\npela adrenalina do momento, você esquece totalmente do desfiladeiro e acaba correndo para a sua morte. "
        "\nVocê acaba caindo e morrendo pelo impacto da queda. ")
        print("\n")
        instrucoes()

    
    
    elif escolha == 2:
        print("Você tenta acertar a figura com uma pedra e consegue. O vulto se esvai e você tenta aproveitar "
        "\nesse tempo para voltar correndo para dentro da casa")
        situacao_2_Sam()
    else:
        print("Escolha uma opção válida")
#Situações que podem ocorrer com o personagem Sam.
def situacao_2_Sam():
    print("você consegue chegar na casa e está completamente aterrorizado. Você tenta alcançar o grupo o mais "
    "\nrápido possível para ficar em segurança. Quando você está chegando na sala você se lembra que trouxe um "
    "\nfacão próprio para trilha e que pode ser usado como arma. O barulho que você ouviu antes volta e ainda mais "
    "\nforte. O que você faz?")
    print("\n")
    escolha2 = int(input("Se você decide ir até o quarto para pegar o facão, digite 1. Caso queira seguir em "
    "\nfrente até o grupo, digite 2: "))
    print("\n")
    if escolha2 == 1:
        print("Você foi para o quarto tentando ser o mais rápido e cauteloso possível, porém quando você entra"
        "\nno quarto, acende a luz e vai até a mala pegar o facão, no canto esquerdo do quarto você vê o vulto "
        "\nolhando fixamente para ti. Já não existe tempo suficiente para reagir. A criatura pula em você e fixa o "
        "\nolhar em seus olhos. Você sente frio e sua força se esvaindo. Você começa a ficar gelado e pálido e "
        "\nconsegue ouvir uma voz que diz: 'Eu vim te buscar'. Após a última palavra dita pela criatura, você morre ")
        print("\n")
        instrucoes()
    elif escolha2 == 2:
        print("Você decide não perder tempo e vai direto para o grupo. Com mais pessoas, mais força para lutar. ")
        situacao_3_Sam()
    else:
        print("Escolha uma opção válida")    
#Situações que podem ocorrer com o personagem Sam e o final da história.
def situacao_3_Sam():
    print("Você chegou ao grupo e começa a contar tudo o que aconteceu. Todos te olham de modo estranho tentando "
    "\nentender o que está acontecendo. Uns ficam assutados, outros não dão tanta bola para o que você está falando "
    "\nVocê tenta de todo modo convencer cada um sobre o perigo que está rondando o local. ")
    teste= float(input("Você deverá escolher um número entre 1 a 7 para medir sua sanidade mental: "))
    sorte = (teste + 1)
    if sorte >= 7:
        print("Você conseguiu convencer seus amigos sobre o que aconteceu. Vocês ficam em grupo e vão para o "
        "\no carro para irem embora o mais rápido possível.")
        print("\n")
        main()
    elif sorte < 7:
        print("Você não conseguiu convencer seus amigos. O impacto da situação e principalmente do olhar "
        "\nda criatura mexeram com a sua sanidade mental. Você já não sabe mais o que é real e o que não é. ")
        instrucoes()

    else:
        print("Digite um número entre 1 e 7")
#Aqui começa a história com a personagem Laurie. Breve introdução e escolhas
def personagem_Laurie():
    print("Você escolheu a Laurie. Laurie é uma garota introvertida e é a que está sempre pelos amigos quando "
    "\nnecessário. Ela ama ler livros e desenhar. Recentemente abriu uma empresa de marketing. ")
    print("\n")
    print("\nCom a lua já no céu e um tempo bem agradavél, seus amigos resolveram ficar perto da fogueira conversando, "
    "\nbebendo e ouvindo música. Você preferiu ficar na rede lendo um livro sobre a história local. "
    "\nVocê leu sobre tudo o que tinha ocorrido, sobre a trágica guerra e massacre ali ocorridos. Leu sobre "
    "\nas lendas e ficou bem vidrada nas histórias. "
    "\nDepois te ter lido um pouco, você decidiu guardar o livro no quarto. Sua bolsa se encontra dentro do armário, "
    "\nvocê a puxa mas além da bolsa uma caixa de aparência bem antiga acaba caindo junto. "
    "\nVocê deixa o livro de lado e começa a mexer na caixa. "
    "\nVocê encontra vários objetos na caixa, desde um boneco de pano como objetos que vão desde anéis a uma carta. "
    "\nVocê acaba lendo o conteúdo da carta que, em suma, diz que nas próximas horas algo irá acontecer com a "
    "\na pessoa que tocou no boneco e nos objetos. A princípio você ignora e vai para a companhia de seus amigos. "
    "\nAlgumas horas se passam e você começa a ouvir sons misteriosos ao redor do ambiente. Você pergunta a um "
    "\nde seus amigos, mas ele não ouve nada. Confrome os minutos vão passando, o barulho fica mais intenso e você "
    "\ncomeça se sentir aflita. "
    "\nDois amigos seus resolvem ir caminhar e dois acabam indo para dentro da casa. Você está sozinha frente "
    "\na fogueira. O que você faz? ")
    print("\n")
    escolha = float(input("Se você decide continuar sozinha frente a fogueira, digite 1. Caso decida seguir "
    "\nseus amigos na caminhada, digite 2: "))
    print("\n")
    if escolha == 1:
        print("Você decidiu ficar em frente a fogueira. Você fica perto da fogueira para se esquentar e tentar "
        "\nesquecer do barulho de alguma forma. Enquanto você encara o fogo, uma figura de uma mulher amarrada em "
        "\num tronco aparace te encarando fixamente. Ela está sendo queimada viva. Você tenta se levantar e se "
        "\nafastar num ato relfexivo, mas você acaba caindo na fogueira. O fogo da fogueira fica muito intenso, "
        "\nseus gritos são totalmente abafados pela presença. Ninguém te ouve e você acaba sendo queimada viva. ")
        print("\n")
        instrucoes()
    elif escolha == 2:
        print("você decide ir caminhar com seus amigos. Acredita que ficar com alguém poderá ajudar ")
        situacao_1_Laurie()
    else:
        print("Escolha uma opção válida.")
#Situações que podem ocorrer com a personagem Laurie.
def situacao_1_Laurie():
    print("Você saiu atrás dos seus amigos. Você tem seu cleular em mãos e o usa pra iluminar o caminho. "
    "\nVocê sabe que seus amigos foram pela direita, mas está bem escuro. A lanterna do seu celular ilumima "
    "\num pouco, mas não o suficente para se ter uma ótima visão do que está a frente. "
    "\nApos você andar uns 13 metros, você consegue visuzaliar duas silhuetas. Ao mesmo tempo você ouve a voz de "
    "\nsua amiga, porém vem da direção oposta das silhuetas. As silhuetas estão do lado direito, a voz do lado "
    "\nesquerdo.")
    print("\n")
    escolha_2 = float(input("Qual caminho você pega? Direita, digite 1. esquerda 2: "))
    print("\n")
    if escolha_2 == 1:
        print("Você viu as silhuetas e pensou que eram seus amigos. Você está errada. "
        "\nTalvez com a possibilidade de ser a ajuda, você se esqueceu que pela direita abrigava uma floresta "
        "\nmuito densa com visibilidade quase nula. Quando você começa a caminhar, a lanterna do celular começa "
        "\na falhar. As figuras se aproximam de ti e param na sua frente. Como em um piscar de olhos, uma figura "
        "\nte pega pelo pescoço e te levanta. Você começa a perder os sentidos até parar de respirar. "
        "\nSeu corpo é jogado ao lado de uma árvore e em cima de seu corpo está um bilhete escrito com sangue "
        "\n 'NÃO MEXA NO QUE NÃO LHE PERTENCE' ")
        print("\n")
        instrucoes()
    elif escolha_2 == 2:
        print("Você decidiu ir pela voz pois sentia mais segurança já que conhecia esta voz há anos. ")
        situacao_2_Laurie()
    else:
        print("escolha uma opção válida ")
#Situações que podem ocorrer com a persongame Laurie e o final da história.
def situacao_2_Laurie():
    print("você decidiu seguir a voz e acabou encontrando seus amigos. Eles te perguntam se algo havia acontecido, "
    "\npois você estava visivelmente atordoada. Você tenta explicar em detalhes o que aconteceu e por fim "
    "\nvocês três voltam para perto da fogueira. Seus amigos conseguiram te acalmar e a princípio tudo parecia bem. "
    "\nUm pouco depois, você foi tentar dormir para tentar esquecer o que tinha acontecido. Você torcia para "
    "\nser um sonho. Porém, quando você está quase dormindo você percebe que tem alguém se aproximando do quarto. "
    "\nVocê tenta ver quem é, mas não consegue. Seu instinto diz que é a mesma criatura que estava perto da floresta "
    "\nmais cedo. O ambiente começa a ficar gélido e uma adrenalina começa a tomar conta do seu corpo. Seu coração acelera. "
    "\nVocê tenta mexer suas pernas mas não consegue. Parece que alguém prendeu suas pernas com fortes algemas. "
    "\nDo lado do seu travesseiro está seu celular. Você sente que seus braços estão normais e tem a possibilidade "
    "\nde pegar o celular. O que você faz? ")
    print("\n")
    escolha_3 = float(input("Se você fica imóvel, digite 1. Caso tente pegar o celular, digite 2. "))
    print("\n")
    if escolha_3 == 1:
        
        print("Você fica imóvel. Você prefere ficar quieta, fingindo que não estava ali. Quem sabe a "
        "\na criatura não passaria direto? E você escolheu certo! Você não se move e torce o máximo possível "
        "\npara a situação acabar. O ambiente gélido aos poucos começa a retomar a normalidade. "
        "\nVocê acaba dormindo e no dia seguinte conta para todos. Vocês resolvem ir embora daquele local o mais "
        "\nrápido possível. ")
        print("\n")
        main()
    elif escolha_3 == 2:
        print("Você decide pegar o celular. Você percebe que seria uma ótima oportunidade para chamar por ajuda. "
        "\nMas assim que você move o braço para pegar, você percebe que a criatura está do seu lado e com um sorriso "
        "\nassustador. Não dá nem tempo de gritar. A criatura passa as unhas em seu pescoço e você começa a sangrar ali mesmo. "
        "\nEm alguns instintantes você estará morta e entrará para a história como mais uma vítima da criatura. ")
        print("\n")
        instrucoes()
    else:
        print("Escolha uma opção válida.")
#Aqui começa a história com o personagem Daniel. Breve introdução e escolhas.
def personagem_Daniel():
    print("Você escolheu o Daniel. Daniel é uma pessoa muito humorada, mas tem seu tempo para ficar consigo mesmo. "
    "\nAtualmente ele trabalha no mercado fincaneiro.")
    print("\n")
    print("Vocês estão jogando conversa fora na sala. Música, comida e muita conversa. Porém você se dá conta "
    "\nque esqueceu de pegar alguns utensílios que ficaram no carro. Você pega a chave que está perto da mesa "
    "\nde centro e vai até o carro. Como é noite e choveu mais cedo, o chão está muito escorregadio e com "
    "\nbaixa visibilidade. Você vai até ao carro com cuidado, abre o porta malas e pega o que estava faltando. "
    "\nAssim que você fecha o porta malas e vira para voltar pra casa, você perecebe dois olhos vermelhos pontiagudos "
    "\nte encarando. Em um primeiro momento você não se assusta, pensa que poder ser algum tipo de animal. "
    "\nVocê vai se aproximando do animal, mas conforme chega perto percebe que não se trata de um animal. Você vê que é "
    "\num humano, ou ao menos aparenta ser. Em sua mão direita, tal figura segura uma éspecie de machete com o que "
    "\nparece ter sangue em toda parte. Você fica atônito. O que você faz? ")
    print("\n")
    escolha_1 = float(input("Se você tenta sair correndo de volta para a casa, digite 1. Caso tente ir para "
    "\ndentro do carro, digite 2: "))
    print("\n")
    if escolha_1 == 1:
        print("Você tentou correr, mas como o chão está muito escorregadio, você acaba caindo. A figura "
        "\nse aproxima de você e te acerta com um golpe fatal no peito. Você morre. ")
        print("\n")
        instrucoes()
    elif escolha_1 == 2:
        print("Você vai se afastando com cautela, mas como a casa está longe, você tenta achar abrigo no carro ")
        situacao_2_Daniel ()
#Situações que podem ocorrer com o personagem Daniel.
def situacao_2_Daniel():
    print("Você conseguiu achar abrigo no carro. Você está dentro do carro com todas as portas trancadas. "
    "\nVocê tenta usar seu telefone para se comunicar com seus amigos mas não consegue. Seu telefone é inútil. "
    "\nPelo retrovisor você percebe a figura se aproximando, mas de repente ela desaparece. Você não entende o que "
    "\nestá acontecendo. Você fica procurando pela figura. Quando você menos percebe, ela aparece em frente ao carro "
    "\ne pula no capô. Você leva um susto e percebe que a figura está tentando entrar no carro. "
    "\nO que você faz? ")
    print("\n")
    escolha_2 = float(input("se você tenta ligar o carro e acelerar com tudo para atropelar a figura, digite 1. "
    "\nCaso você permaneça no carro para pensar em outra estratégia, digite 2. "))
    print("\n")
    if escolha_2 == 1:
        print("Você pensa em ligar o carro e atropelar a criatura. Você liga o carro e tenta acelerar o máximo "
        "\npossível, mas como a estrada não está tão boa o carro demora a pegar velocidade. Mas quando o carro "
        "\npega velocidade, a aceleração foi tanta que você realmente atropela a figura, mas acaba indo em direção "
        "ao precipício. Você não consegue frear a tempo e o carro acaba caindo. Você atingiu a criatura, mas acabou "
        "\nmorrendo")
        print("\n")
        instrucoes()
    elif escolha_2 == 2:
        print("Você optou por tentar outra abordagem. Por mais que a figura ainda esteja em sua frente, você "
        "\ntem alguns minutos para que possar pensar em algo. ")
        situacao_3_Daniel ()
#Situações que podem ocorrer com o personagem Daniel e o final da história.
def situacao_3_Daniel():
    print("Você está dentro do carro e abre a mochila de utensílos torcendo para que ache algo útil. "
    "\nVocê procura na mochila e não encontra nada muito valioso, mas olha para o banco de trás e encontra uma "
    "\narma de caça. Você logo reconhece e vê que essa arma é do seu amigo que gosta de praticar caça. "
    "\nA arma tem apenas uma munição e você planeja usar da melhor maneira possível. ")
    print("\n")
    escolha_3 = float(input("Se você decide acender todas as luzes do carro e esperar uma oportunidade para atirar, "
    "\ndigite 1. Caso você saia do carro para poder atirar de uma vez, digite 2. "))
    print("\n")
    if escolha_3 == 1:
        print("Você resolve esperar a melhor oportunidade e ilumina o ambiente a sua volta. A figura dá mais um "
        "\npulo e quebra o vidro. Ela coloca a cabeça entre o espaço feito e neste momento você pega a arma e atira. "
        "\nFoi um tiro certeiro. Você acaba atingindo a figura e vai verificar o que era aquele ser. Quando você "
        "\nchega perto, a figura começa a se desfazer por inteiro. Você percebe que o que quer que seja aquilo, "
        "\nnão trará problemas novamente. ")
        main()
    elif escolha_3 == 2:
        print("Você prefre sair do carro, mas como você não consegue ver direito, o primeiro vulto que você vê "
        "\nvocê atira. Você acaba acertando fatalmente seu amigo que estava vindo te procurar, já que fazia um tempo "
        "\nque você não tinha voltado. Logo após o disparo, você ouve uma gargalhada diabólica vindo do seu lado. "
        "\nJá não existe mais tempo para nada. A figura te acerta no coração. Você cai morto ao lado do seu amigo. ")
        print("\n")
        instrucoes()
#Função para voltar ao ínicio.
main()