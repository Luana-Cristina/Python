print('-------------------------------------------------')
print('Vamos contar as letras das palavras com no máximo 10 caracteres?')
print('-------------------------------------------------')

p1 = input("Informe a primeira palavra: ")
print('-------------------------------------------------')
p2 = input("Infome a segunda palavra: ")
print('-------------------------------------------------')

if len(p1) + len(p2) <= 10:
    valor = int(len(p1) + len(p2))
    print(f"As palavras informadas possuem {valor} caracteres no total!")
else:
    print("Exedeu o limite de caracteres!")
