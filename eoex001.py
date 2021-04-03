# 1)Entrada de dados
valor_total = float(input("Informe o valor total: "))

# 2) Processamento

#calcular valor a vista
#valor_a_vista = valor_total  - (valor_total * 0.1)
valor_a_vista = valor_total * 0.9

#calculo parcelas
valor_parcelado = valor_total / 3

#calcula comissão
valor_comissao = valor_total * 0.05 

# 3) Saida de dados
print ("VALOR A VISTA: R$ {:.2f}".format(valor_a_vista))
print ("3 parcelas de: R$ {:.2f}".format(valor_parcelado))
print ("COMISSÃO: R$ {:.2f}".format(valor_comissao))

if valor_comissao > 100:
    print ("Sua comissão ultrapassou os valores permitidos! ")
