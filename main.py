opcao = 1

manifestacao = [ ]

while opcao != 6:
    print("\nOuvidoria")
    print ("1) Listar Manifestação \n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Remover Manifetação \n5) Substituir Manifetação \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        if len(manifestacao) == 0:
            print("Nao existem manifestações a serem exibidas")
        else:
            print("Lista de Manifestações")
            for item in manifestacao:
                print("-", item)

    elif opcao == 2:
        novaManifestacao = input("Digite a sua Manifestacao: ")
        manifestacao.append(novaManifestacao)
        print("Manifestação adicionada com sucesso!")

        print(len(manifestacao))

    elif opcao == 3:
        codigo = int(input("Digite o código da manifestação a ser pesquisada: "))

        manifestacaoPesquisada = manifestacao[codigo - 1]

        print("A manisfestação pesquisada2 foi:", manifestacaoPesquisada)

    elif opcao == 4:
        codigo = int(input("Digite o codigo da maniofestação a ser removida: "))

        if codigo >= 1 and codigo <= len(manifestacao):
            manifestacao.pop(codigo - 1)
            print("A manifestação foi removida com sucesso!")

        else:
            print("O codigo informado é invalido.")

    elif opcao == 5:
        codigo = int(input("Digite o codigo da manifestação a ser substituida: "))

        if codigo >= 1 and codigo <= len(manifestacao):
            novaManifestacao = input("Digite o nome da nova manifestacao: ")
            manifestacao[codigo - 1] = novaManifestacao
            print("Manifestacao substituida comn sucesso! ")

        else:
            print("O código informado é invalido.")

    elif opcao != 6:
        print("Opção Invalida")

    print("Obrigado por usar a Ouvidoria!")