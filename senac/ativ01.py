usuario = "Senac"
print('-------------------------------------------------')
print("        ------- Faça seu LOGIN -------")
login = input("Login: ")
password = input("Senha: ")
print('-------------------------------------------------')

if login == usuario and len(password) <= 6:
    print("ACESSO LIBERADO!!")
else:
    print("ACESSO INVÁLIDO!!")
