#ETAPA_1#

def obter_limite():
  print ('-------------------------------------------------------------------')
  print ( "======== Bem-vindo a loja de utensílios doméstico, prazer sou a Luana Cristina Faria da Silva, vamos iniciar as compras? ========")
  print ('-------------------------------------------------------------------')
  print ("Vamos fazer uma análise de crédito?")
  print ("Iremos precisar de algumas informaçoes suas...")
  print ('-------------------------------------------------------------------')
  #dados do cliente
  cargo = input ("Informe o cargo que atua na sua empresa: ")
  print ("Cargo: " + cargo)
  print ('___________________________________________________________________')
  salario = float (input ("Informe o seu salário mensal: "))
  print ("Salário: R${:.2f}".format(salario))
  print ('___________________________________________________________________')
  anonasc = int (input ("Informe o ano do seu nascimento: "))
  print ("Ano de nascimento: {}".format(anonasc))
  print ('-------------------------------------------------------------------')
  #ETAPA_2#
  #onde esta sendo definido o limite de gastos
  #calculo da idade
  idade = 2021 - anonasc
  #calculo do limite de gastos
  limiteg = (salario*( idade / 1000 )+100)
    #imprime as informações
  print ("Sua idade aproximada é: {} anos." .format(idade))
  print ('-------------------------------------------------------------------')
  print ("            A N A L I S A N D O    D A D O S    ")
  print ('-------------------------------------------------------------------')
  print ("Seu limite de gasto na loja é R${:.2f}" .format(limiteg))
  print ('-------------------------------------------------------------------')
  print ("*************       Agora vamos as compras?       ****************")
  print ('-------------------------------------------------------------------')
  return limiteg, idade


#etapa3#
def verificar_produto(limite):
  #onde o cliente vai informar o produto e o preço
  print("-----------------------------------------------------------------")
  nome_produto = input("Digite o nome do produto que deseja comprar: ")
  preco_produto = int(input("Digite o preço do produto: "))
  print("-----------------------------------------------------------------")
  print("Produto: {} no valor de R${:.2f}".format(nome_produto, preco_produto))
  print("-----------------------------------------------------------------") 
  porc = ((preco_produto)/(limite)*100)
  if porc <= 60:
    print ("Liberado!") 
  elif  porc > 60 and porc <= 90:
    print ("Liberado ao parcelar em até duas vezes!")
  elif porc > 90 and porc <= 100:
    print ("Liberado ao parcelar em 3 ou mais vezes!")
  else:
    print ("Bloqueado!")

  #utilizando meu nome para calcular o desconto do cliente

  completo = ('LuanaCristinaFariadaSilva')
  numnome= len(completo)
  primeiro_nome = ('Luana')
  numprim = float(len(primeiro_nome))
  desconto = preco_produto - numprim
  if preco_produto < numnome and preco_produto < idade:
    print("Você recebeu um desconto de R${:.2f}".format(numprim))
    print("Preço do produto agora é {:.2f}".format(desconto))
  else:
    print("Poxa :( não conseguimos um desconto....") 
  return preco_produto
  
#ETAPA4#
limite, idade = obter_limite()
preco_produto = verificar_produto(limite)
compras = int(input("Quantos produtos deseja cadastrar?"))
print (compras)
total = 0
cont = 0
for cont in range(compras):
  #total dos valores dos produtos
  total += preco_produto
  #chamar verificar_produto
  disp = verificar_produto(limite) - total
  if (verificar_produto(limite) < disp):
    print ('Limite excedido...')
  else:
    print('Obrigada, volte sempre...')
    break