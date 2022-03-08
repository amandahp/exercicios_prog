# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. # noqa


def notas():
    nota = float(input("Insira uma nota, entre 0 e 10: "))
    while nota < 0 or nota > 10:
        nota = float(input("Insira uma nota, entre 0 e 10: "))
        if nota > 0 and nota < 10:
            break
    print(f"A nota é: {nota} ")

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. # noqa


def nome_senha(nome, senha):
    while nome == senha:
        senha = (input(f'''
        {ValueError}
        Senha inválida. Insira uma nova senha: '''))
        if senha != nome:
            break
    print(f"Seu nome é: {nome}. Sua senha é: {senha}")


# Faça um programa que leia e valide as seguintes informações:
    '''
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; ''' # noqa

def validando_info(nome, idade, salario, sexo, estado_civil): # noqa
    while len(nome) < 3:
        nome = str(input(f'{nome} é inválido. Insira o seu nome completo: '))
        if len(nome) > 3:
            break
    while idade < 0 or idade > 150:
        idade = int(input(f'{idade} é inválido. Insira a idade correta: '))
        if idade > 0 and idade < 150:
            break
    while salario < 0:
        salario = float(input(f'{salario} é inválido. Insira o salário correto: ')) # noqa
        if salario > 0:
            break
    while len(sexo) >= 0:
        if sexo == "f" or sexo == "m":
            break
        else:
            sexo = str(input(f'{sexo} é inválido. Insira o sexo correto:(f/m) ')) # noqa
            continue
    while len(estado_civil) >= 0: # noqa
        if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d": # noqa
            break
        else:
            estado_civil = str(input(f'{estado_civil} É um dado inválido. Insira o estado civil correto:(s/c/v/d) ')) # noqa
            continue
    print(f'''
        Nome: {nome};
        Idade: {idade};
        Salário: {salario};
        Sexo: {sexo};
        Estado Civil: {estado_civil}.''')


'''Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas
de crescimento. ''' # noqa


def a_b():
    pais_a = 80000
    pais_b = 200000
    i = 0
    while pais_a != pais_b:
        pais_a += (pais_a*0.03)
        pais_b += (pais_b*0.015)
        i += 1
        if pais_a >= pais_b:
            print(f"Anos necessário para que as população dos países seja igualada: {i}") # noqa
            break
        else:
            continue

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. # noqa


def input_a_b():
    populacao_1 = int(input("Insira a população do País 1: "))
    taxa_1 = float(input("Insira a taxa de crescimento anual da população do País 1: ")) # noqa
    populacao_2 = int(input("Insira a população do País 2: "))
    taxa_2 = float(input("Insira a taxa de crescimento anual da população do País 2: ")) # noqa
    i = 0
    while populacao_1 != populacao_2:
        populacao_1 += (populacao_1*(taxa_1/100))
        populacao_2 += (populacao_2*(taxa_2/100))
        i += 1
        if populacao_1 >= populacao_2:
            print(f"Anos necessário para que as população dos países seja igualada: {i}") # noqa
            break
        else:
            continue

# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. # noqa


def intervalo():
    for i in range(1, 20):
        print(i)

# Depois modifique o programa para que ele mostre os números um ao lado do outro. # noqa


def intervalo_lista():
    lista = []
    for i in range(1, 20):
        lista.append(i)
    print(lista)


# Faça um programa que leia 5 números e informe o maior número.

def numbers():
    numeros = [2, 2, 7, 6, 10]
    print(max(numeros))


def n():
    lista = []
    for i in range(0, 5):
        valor = int(input(f'Digite o número {i+1}: '))
        lista.append(valor)
    print(f"O maior número da lista é {max(lista)}")


# Faça um programa que leia 5 números e informe a soma e a média dos números. # noqa

def media_soma():
    lista = []
    for i in range(0, 5):
        valor = int(input(f'Digite o número {i+1}: '))
        lista.append(valor)
    soma = sum(lista)
    media = soma / 5
    print(f'''
      Valores: {lista}
      Soma: {soma}
      Media: {media}
    ''')


# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. # noqa


def impares():
    impares = []
    for i in range(1, 50):
        if (i % 2) != 0:
            impares.append(int(i))
    for n in impares:
        print(n)


# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. # noqa

def inteiros():
    n_1 = int(input("Digite o numero 1: "))
    n_2 = int(input("Digite o numero 2: "))
    inteiros = []
    for i in range(n_1, n_2):
        if i//1 == i:
            inteiros.append(i)
    for j in inteiros:
        print(j)


'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja 
ver a tabuada''' # noqa

# para todas as tabuadas de uma vez


def tabuada():
    v_tabuada = int(input("Qual tabuada você gostaria de criar? "))
    tabuada = []
    if v_tabuada < 10:
        for i in range(0, 11):
            resultado = v_tabuada * i
            tabuada.append(f"{v_tabuada} x {i} = {resultado}")
    else:
        for i in range(0, v_tabuada+1):
            resultado = v_tabuada * i
            tabuada.append(f"{v_tabuada} x {i} = {resultado}")
    for j in tabuada:
        print(j)
