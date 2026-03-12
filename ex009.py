cod_vendedor = input("Insira o código de identificação do vendedor: ")
qnt_produto = int(input("Insira quantos produtos foram vendidos pelo vendedor: "))

valor_produto = 100.00

valor_total = qnt_produto * valor_produto
comiss = valor_total * 0.15

print("O código de identificação do vendedor é: ", cod_vendedor, ".")
print("A quantidade de produtos vendidos foi ", qnt_produto, "Fones de Ouvido.")
print("O valor total da venda foi de R$", valor_total, ".")
print("A comissão do vendedor é de R$", comiss, ".")
