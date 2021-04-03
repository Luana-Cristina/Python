# 1-Entrada de dados
r = float(input("Informe o raio do cilindro(cm):"))
h = float(input("Informe a altura (cm):"))

# 2-Processamento
import math
volume = math.pi * (r**2) * h

# 3-Saída de dados

print ("Volume: {:.2f}cm3".format(volume))

if volume <= 10:
    print ("Mova o cilindro para o GALPÃO 1! ")
elif volume > 10 and volume < 15:
     print ("Mova o cilindro para o GALPÃO 2! ")
else:
     print ("Mova o cilindro para o GALPÃO 3! ")
