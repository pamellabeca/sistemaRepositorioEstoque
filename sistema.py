print("Bem vindo ao Controle de Estoque da Bicicletaria da Pamella Rebeca Bispo da Silva Nacimento\n")

#função de cadastrar peça
def cadastrarPeca(codigo):
    dadosPeca = {}
    print("Você Selecionou a Opção de Cadastrar Peça")
    print("Código da Peça", str(codigo).zfill(3)) #vão ser adicionados dois 0 antes do código que é definido pelo contador

    #definidos valores para suas respectivas 
    nome = str(input("Por favor entre com o NOME da peça: "))
    fabricante = str(input("Por favor entre com o FABRICANTE da peça: "))
    valor = float(input("Por favor entre com o VALOR(R$) da peça: "))

    #armazenadas variáveis no dicionário
    dadosPeca["codigo :"] = str(codigo).zfill(3)
    dadosPeca["nome :"] = nome
    dadosPeca["fabricante :"] = fabricante
    dadosPeca["valor :"] = valor

    return dadosPeca

#função de consultar peça
def consultarPeca(dadosPeca):
    print("Você Selecionou a Opção de Consultar Peça")
    while True:

        #menu
        print("Escolha a opção desejada:")
        print("1. Consultar Todas as Peças")
        print("2. Consultar Peças por Código")
        print("3. Consultar Peças por Fabricante")
        print("4. Retornar")

        #escolha da opção do menu
        escolha = int(input())

        #escolha de consultar todas as peças
        if escolha == 1:
            print("--------------------")
            for peca in dadosPeca.values():
                print(f"Código: {peca['codigo :']}")
                print(f"Nome: {peca['nome :']}")
                print(f"Fabricante: {peca['fabricante :']}")
                print(f"Valor: R${peca['valor :']}")
                print("--------------------")

        #escolha de consultar as peças pelo código
        elif escolha == 2:
            numero = str(input("Digite o CÓDIGO da peça: ")).zfill(3)
            peca = dadosPeca.get(numero)
            
            if peca in dadosPeca.values():
                print("--------------------")
                print(f"Código: {peca['codigo :']}")
                print(f"Nome: {peca['nome :']}")
                print(f"Fabricante: {peca['fabricante :']}")
                print(f"Valor: R${peca['valor :']}")
                print("--------------------")
            else:
                print("--------------------")
                print("Peça não encontrada")
                print("--------------------")

        #escolha de consultar as peças pelo fabricante
        elif escolha == 3:
            fabrica = str(input("Digite o FABRICANTE da peça: "))

            for peca in dadosPeca.values():
                if peca["fabricante :"] == fabrica:
                    print("--------------------")
                    print(f"Código: {peca['codigo :']}")
                    print(f"Nome: {peca['nome :']}")
                    print(f"Fabricante: {peca['fabricante :']}")
                    print(f"Valor: R${peca['valor :']}")
            print("--------------------")
        elif escolha == 4:
            break

#função de remover peça
def removerPeca(dadosPeca):
    print("Você Selecionou a Opção de Remover Peça")
    remover = str(input("Digite o código da peça a ser removida: "))

    codigo_remover = remover.zfill(3) #formata o código da variável remover com zeros à esquerda, se for preciso
    chave = codigo_remover
    if chave in dadosPeca: #analisa se a chave está dentro do dicionário
        del dadosPeca[chave] #remove a peça do dicionário
    
def principal():
    global codigo
    codigo = 1
    dadosPeca = {} #dicionário para armazenar as peças cadastradas

    #menu
    while True:
        print("Escolha a opção desejada:")
        print("1. Cadastrar Peças")
        print("2. Consultar Peças")
        print("3. Remover Peças")
        print("4. Sair")

        escolha = int(input()) #armazena a opção escolhida pelo usuário
        if escolha == 1:
            peca = cadastrarPeca(codigo) #chama a função cadastrarPeca, passando o código atual
            dadosPeca[peca["codigo :"]] = peca #adiciona a peça ao dicionário e usa o código como chave
            codigo += 1 #incrementa o código para a próxima peça

        elif escolha == 2:
            consultarPeca(dadosPeca) #chama a função consultarPeca, passando o dicionário de peças
        elif escolha == 3:
            removerPeca(dadosPeca) #chama a função removerPeca, passando o dicionário de peças
        elif escolha == 4:
            break #sai do loop principal e encerra o programa
    
principal()