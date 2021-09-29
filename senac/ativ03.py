nome = input("Informe seu nome: ")
sobrenome = input("Infome seu sobrenome: ")

if len(nome) + len(sobrenome) <= 10:
    valor = int(len(nome) + len(sobrenome))
    print(f"valido {valor}")
else:
    print("erro")