cod_pec = input("Insira o código da peça: ")
valor = float(input("Insira o valor da peça: "))
qnt = int(input("Insira a quantidade que pretende adquirir: "))

valor_total = qnt * valor

print("O total a pagar é de R$", valor_total, "pela peça de código {}.".format(cod_pec))
