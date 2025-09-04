manifestacao = ["nao gosto dele", "eu gosto dele"]

if len (manifestacao) == 0:
    print("Nao existem manifestações a serem exibidas")
else:
    print("Lista de Manifestações")
    for item in manifestacao:
        print("-",item)