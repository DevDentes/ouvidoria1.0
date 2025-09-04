manifestacao = ["Abella nao é um bom professor", "Adoro fazer programa!"]

codigo = int(input("Digite o codigo da maniofestação a ser removida: "))

if codigo >= 1 and codigo <= len(manifestacao):
    manifestacao.pop(codigo-1)
    print("A manifestação foi removida com sucesso!")

else:
    print("O codigo informado é invalido.")