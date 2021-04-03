nomeloja= "Bem-vindo a loja da Luana Cristina Faria da Silva"

print (nomeloja)
print ("Vamos fazer uma análise de crédito?")

cargo = input ("Informe o cargo que atua na sua empresa: ")
salario = float (input ("Informe o seu salário[sem pontos e vírgulas]: "))
anonasc = int (input ("Informe o ano do seu nascimento: "))

print ("Cargo: " + cargo)
print ("Salário: ", salario)
print ("Ano de nascimento: ", anonasc)
#etapa2#

idade = 2021 - anonasc
limiteg =((salario * (1.000 / idade)) + 100)
print ("Idade:{} " .format(idade))
print ("Seu limite de gasto na loja é {:.2f}" .format (float(limiteg)))

#etapa3#
