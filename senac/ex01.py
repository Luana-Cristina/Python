#Atividade input Luana Cristina

print("Informe seus dados:")
print("------------------------------------")
nome = input("Digite seu nome: ")
profissao = input("Qual a sua profissão: ")
salario = float(input("Qual o seu salário: "))
aumento = (salario * 0.10) + salario
empresa = int(input("Está a quantos anos na empresa: "))
print("------------------------------------")
print("Dados do funcionário")
print("------------------------------------")
print(f"Nome: {nome}\nProfissão: {profissao}\nSalário com aumento de 10%: {aumento:.2f}\nEstá na empresa a {empresa} ano(s).")
print("------------------------------------")
