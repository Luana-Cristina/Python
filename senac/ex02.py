print('------------------------------------------------')
print('Informaremos seu cargo de acordo com seu salário')
print('------------------------------------------------')

salario = float(input('Informe o seu salário: '))

print('------------------------------------------------')


if salario <= 1600:
    print('Você é Auxiliar de Limpeza!')
    print('------------------------------------------------')
elif salario > 1600 and salario <=2000:
    print('Você é Auxiliar Administrativo!')
    print('------------------------------------------------')
elif salario > 2000 and salario <= 3500:
    print('Você é de Supervisor!')
    print('------------------------------------------------')
elif salario >= 3501 and salario <= 5000:
    print('Você é Programador!')
    print('------------------------------------------------')
elif salario > 5000:
    print('Você é Sócio da Empresa!')
    print('------------------------------------------------')
else:
    print('Salário informado não corresponde a nenhum cargo da empresa!')
    print('------------------------------------------------')