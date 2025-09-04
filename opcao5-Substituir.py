manifestacao = ["Abella nao é um bom professor", "Adoro fazer programa!"]

codigo = int(input("Digite o codigo do filme a ser substituido: "))

if codigo >=1 and codigo <= len(manifestacao):
    novaManifestacao = input("Digite o nome da nova manifestacao: ")
    manifestacao[codigo-1] = novaManifestacao
    print("Manifestacao substituida comn sucesso! ")

else:
    print("O código informado é invalido.")
