nomeloja = input("Informe o nome da loja: ")
anofundacao = (input("Informe o ano de fundação da loja: "))
distancia = float(input ("Informe a distância da loja: "))
tempo = float (input ("Informe o tempo até a loja(h)"))

#Comentários de código 
#print("Nome da Loja: " + nomeloja)
#print("Ano Fundação: " +str (anofundacao))
#print("Distância: {:.2f}km".format(distancia))


print("Nome da loja: {0}\nAno: {1}\nDistância: {2}km".format(nomeloja, anofundacao, distancia))

# vm = distancia/tempo
vm = distancia/tempo

print("Velocidade média: {:2.2f}km/h".format(vm))

media =  (10 + 20 + 30) / 3

print("Média: {:.2f}".format (media))
