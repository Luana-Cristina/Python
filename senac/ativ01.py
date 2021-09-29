usuario = "Senac"

login = input("Login: ")
password = input("Senha: ")

if login == usuario and len(password) <= 6:
    print("Acesso liberado!")
else:
    print("Acesso inválido!")