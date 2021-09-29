print('-------------------------------------------------')
print('------ Cadastro de Alunos Maiores de Idade ------')
print('-------------------------------------------------')
list = []
cont = 0
while cont < 10:
    idade = int(input("Informe a idade do aluno: "))
    list.append(idade)
    if idade >= 18:
        cont = cont + 1
    else:
        print('Idade inválida')
print('-------------------------------------------------')
print("Cadastros realizados")
print(f"\nForam cadastrados {list.count(18)} alunos com 18 anos!")
print('-------------------------------------------------')

