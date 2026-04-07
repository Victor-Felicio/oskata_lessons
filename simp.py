# Sistema Interativo Multifuncional em Python (S.I.M.P.).

import random
import json

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite um número válido.")


def ler_lista_numeros():
    while True:
        entrada = input("Digite números separados por espaço: ")
        try:
            return list(map(float, entrada.split()))
        except ValueError:
            print("Erro: digite apenas números.")


def ler_opcao(opcoes_validas):
    while True:
        opcao = input("Escolha: ")
        if opcao in opcoes_validas:
            return opcao
        else:
            print("Opção inválida!")

# Lista para manipulação de dados.

lista_nomes = []


# FUNÇÕES MATEMÁTICAS.
def somar():
    a = ler_float("Digite o primeiro número: ")
    b = ler_float("Digite o segundo número: ")
    print("Resultado:", a + b)

def par_ou_impar():
    n = ler_inteiro("Digite um número: ")
    if n % 2 == 0:
        print("Número par.")
    else:
        print("Número ímpar.")

def media():
    lista = ler_lista_numeros()

    if not lista:
        print("Lista vazia!")
        return

    print("Média:", sum(lista) / len(lista))

def fatorial():
    n = ler_inteiro("Digite um número: ")

    if n < 0:
        print("Não existe fatorial de número negativo.")
        return

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    print("Fatorial:", resultado)

def primo():
    n = ler_inteiro("Digite um número: ")

    if n < 2:
        print("Não é primo.")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Não é primo.")
            return

    print("É primo.")

def maior_menor():
    lista = ler_lista_numeros()

    if not lista:
        print("Lista vazia!")
        return

    print("Maior:", max(lista))
    print("Menor:", min(lista))

# TEXTO.
def contar_vogais():
    texto = input("Digite uma palavra: ").lower()
    vogais = "aeiou"
    contador = sum(1 for letra in texto if letra in vogais)
    print("Quantidade de vogais:", contador)


def inverter_texto():
    texto = input("Digite um texto: ")
    print("Invertido:", texto[::-1])


def contar_palavras():
    frase = input("Digite uma frase: ")
    print("Quantidade de palavras:", len(frase.split()))


# DADOS.
def adicionar_nomes():
    while True:
        nome = input("Digite um nome (ou 'sair' para parar): ")
        if nome.lower() == 'sair':
            break
        lista_nomes.append(nome)
        salvar_dados()
    print("Lista atual: ", lista_nomes)
    print("Nome adicionado!")


def remover_nome():
    if not lista_nomes:
        print("A lista está vazia.")
        return
    print("Lista atual: ", lista_nomes)
    nome = input("Digite o nome que deseja remover: ")
    if nome in lista_nomes:
        lista_nomes.remove(nome)
        salvar_dados()
        print("Nome removido.")
    else:
        print("Nome não encontrado.")
    print("Lista atual: ", lista_nomes)


# EXTRAS.
def numero_aleatorio():
    print("Número aleatório: ", random.randint(1, 100))


def login_simples():
    usuario_correto = "Victor"
    senha_correta = "8118"

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

def salvar_dados():
    dados = {
        "nomes": lista_nomes
    }
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def carregar_dados():
    global lista_nomes
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            lista_nomes = dados.get("nomes", [])
    except FileNotFoundError:
        lista_nomes = []


#  MENUS.

def menu_matematica():
    while True:
        print("=== MENU MATEMÁTICA ===")
        print("1 - Somar dois números")
        print("2 - Par ou ímpar")
        print("3 - Média de números")
        print("4 - Fatorial")
        print("5 - Número primo")
        print("6 - Maior e menor número")
        print("0 - Voltar")

        opcao = ler_opcao(["1", "2", "3", "4", "5", "6", "0"])

        if opcao == "1":
            somar()
        elif opcao == "2":
            par_ou_impar()
        elif opcao == "3":
            media()
        elif opcao == "4":
            fatorial()
        elif opcao == "5":
            primo()
        elif opcao == "6":
            maior_menor()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_texto():
    while True:
        print("=== MENU TEXTO ===")
        print("1 - Contar vogais.")
        print("2 - Inverter texto.")
        print("3 - Contar palavras.")
        print("0 - Voltar.")

        opcao = ler_opcao(["1", "2", "3", "0"])

        if opcao == "1":
            contar_vogais()
        elif opcao == "2":
            inverter_texto()
        elif opcao == "3":
            contar_palavras()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_dados():
    while True:
        print("=== DADOS ===")
        print("1 - Adicionar nomes.")
        print("2 - Remover nome.")
        print("0 - Voltar.")

        opcao = ler_opcao(["1", "2", "0"])

        if opcao == "1":
            adicionar_nomes()
        elif opcao == "2":
            remover_nome()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_extras():
    while True:
        print("=== EXTRAS ===")
        print("1 - Criar número aleatório de 1 a 100.")
        print("2 - Login.")
        print("0 - Voltar.")

        opcao = ler_opcao(["1", "2", "0"])

        if opcao == "1":
            numero_aleatorio()
        elif opcao == "2":
            login_simples()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        print("=== OPÇÕES: ===")
        print("1 - Operações Matemáticas.")
        print("2 - Manipulação de Texto.")
        print("3 - Manipulação de Dados.")
        print("4 - Extras.")
        print("0 - Encerrar.")

        opcao = ler_opcao(["1", "2", "3", "4", "0"])

        if opcao == "1":
            menu_matematica()
        elif opcao == "2":
            menu_texto()
        elif opcao == "3":
            menu_dados()
        elif opcao == "4":
            menu_extras()
        elif opcao == "0":
            salvar_dados()
            print("Dados salvos. Até mais!")
            break

        else:
            print("Opção inválida!")

carregar_dados()
main()