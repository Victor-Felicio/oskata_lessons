nome = input("Digite o seu nome: ")
matri = input("Digite o número da sua matrícula: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

menor = min(nota1, nota2, nota3)

nota_final = (nota1 + nota2 + nota3 - menor) / 2

print("Seu nome é: {}.".format(nome))
print("O número da sua matrícula é: ", matri, ".")
print("Sua nota final é: ", nota_final, ".")
