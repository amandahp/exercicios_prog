import math
import re
import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def indices_reais(string_list):
    lista_indice = list([])
    for elem in string_list:
        if elem in string_list:
            counter = 0
            elem_pos = []
        for i in string_list:
            if i == elem:
                elem_pos.append(counter)
            counter = counter + 1
        lista_indice += elem_pos
    nova_lista = (sorted(set(lista_indice)))
    return nova_lista


# Faça um Programa que mostre a mensagem "Alo mundo" na tela.


def mensagem(msg: str) -> str():
    return print(msg)


# mensagem("Alo mundo")


# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. # noqa

def seu_numero() -> str():
    numero = input("Digite um número: ")
    return print(f'O número informado foi: {numero}')


# seu_numero()


# Faça um Programa que peça dois números e imprima a soma.

def soma_de_dois_numeros() -> str:
    n1 = input("Digite um valor: ")
    n2 = input("Digite mais um valor: ")
    return print(f'A soma dos números {n1} e {n2} é: {int(n1)+int(n2)}')


# soma_de_dois_numeros()


# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media_das_notas():
    nota1 = input("Nota PROVA 1: ")
    nota2 = input("Nota PROVA 2: ")
    nota3 = input("Nota PROVA 3: ")
    nota4 = input("Nota PROVA 4: ")
    media_bimestre = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4
    return print(f'A média bimestral é: {media_bimestre}')


# media_das_notas()

# ou


def media_notas():
    qtd_provas = input("Quantas provas foram feitas no bimestre? ")
    notas_provas = list([])
    provas = int(qtd_provas)
    for i in range(0, provas):
        notas = input(f'Digite a nota da PROVA {i+1}: ')
        notas_int = int(notas)
        notas_provas.append(notas_int)
    return print(f'A média das provas é: {sum(notas_provas) / len(notas_provas)}') # noqa


# media_notas()


# Faça um Programa que converta metros para centímetros.


def converte_m_p_cm():
    valor_metros = input("Digite o valor em metros: ")
    valor_cm = int(valor_metros) * 100
    unidade_de_medida = str()
    if int(valor_metros) < 2:
        unidade_de_medida = "metro"
    else:
        unidade_de_medida = "metros"
    return print(f'O valor {valor_metros} em {unidade_de_medida}, corresponde a {valor_cm} centimetros') # noqa


# converte_m_p_cm()


# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


def calculando_a_area_do_circulo():
    valor_raio = input("Digite o valor do raio da circunferência: ")
    area_circunferencia = math.pi * (int(valor_raio) ** 2)
    return print(f'A área da circunferência de raio com o valor {valor_raio} é: {area_circunferencia} m^2') # noqa


# calculando_a_area_do_circulo()


# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. # noqa


def area_de_um_quadrado_ao_dobro():
    valor_aresta_quadrado = input("Digite o valor da aresta do quadrado: ")
    area_quadrado = int(valor_aresta_quadrado) ** 2
    return print(f'O dobro da área de um quadrado de {area_quadrado} é: {area_quadrado*2}') # noqa


# area_de_um_quadrado_ao_dobro()


# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. # noqa


def calculo_salario():
    valor_hora = input("Digite o valor recebido por hora: ")
    horas_trabalhadas_mes = input("Quantas horas foram trabalhadas no mês? ")
    salario_mensal = float(valor_hora) * float(horas_trabalhadas_mes)
    return print(f'O salário do mês será equivalente a: R$ {float(salario_mensal)}') # noqa


# calculo_salario()

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. # noqa
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. # noqa


def fahrenheit_celsius():
    unidade_temp = input("Qual unidade está a temperatura que deseja converter?(Celsius/Fahrenheit) ") # noqa
    if unidade_temp == "Fahrenheit" or unidade_temp == "fahrenheit" or unidade_temp == "Celsius" or unidade_temp == "celsius": # noqa
        temperatura = input(f"Digite o valor da temperatura em graus {unidade_temp}: ") # noqa
        temperatura_float = float(temperatura)
    if unidade_temp == "Fahrenheit" or unidade_temp == "fahrenheit":
        print(f'A temperatura {temperatura_float} em graus Fahrenheit, será convertida para graus Celsius.') # noqa
        temperatura_celsius = (temperatura_float-32)/1.8
        return print(f'A temperatura {temperatura_float}°F equivale a  {round(temperatura_celsius, 2)}°C') # noqa
    elif unidade_temp == "Celsius" or unidade_temp == "celsius":
        print(f'A temperatura {temperatura_float} em graus Celsius, será convertida para graus Fahrenheit.') # noqa
        temperatura_fahrenheit = temperatura_float * 1.8 + 32
        return print(f'A temperatura {temperatura_float}°C equivale a  {round(temperatura_fahrenheit, 2)}°F') # noqa
    else:
        print("Opção inválida")


# fahrenheit_celsius()


# Programa numeros
''' Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: # noqa
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. '''


def numeros():
    lista_int = list([])
    lista_real = list([])
    lista_todos = list([])
    contador = 0
    while contador < 2:
        if len(lista_int) < 1:
            number_int = input("Digite um número inteiro: ")
            if not is_int(number_int):
                print("Número inválido.")
                continue
            lista_int.append(int(number_int))
        number_int = input("Digite outro número inteiro: ")
        if not is_int(number_int):
            print("Número inválido.")
            continue
        lista_int.append(int(number_int))
        break
    numero_real = (input("Digite um número real: "))
    if (bool(re.search(",", numero_real))):
        number_convert = numero_real.replace(",", ".")
        numero_real = number_convert
    else:
        numero_real = numero_real
    if is_number(numero_real):
        numero_real = float(numero_real)
    else:
        print("Número inválido")
        print("O programa será reinicializado")
        print("---------------------------\n")
        restart_program()
    if ((numero_real) // 1 == numero_real):
        numero_real = int(numero_real)
    else:
        numero_real = float(numero_real)
    lista_real.append(numero_real)
    lista_todos = lista_int + lista_real
    if isinstance(lista_todos[0], int) and isinstance(lista_todos[1], int) and isinstance(lista_todos[2], int) or isinstance(lista_todos[2], float): # noqa
        produto = lista_todos[0]*2 + (lista_todos[1]/2)
        if (float(produto) // 1 == produto):
            produto = int(produto)
        soma = lista_todos[0]*3 + lista_todos[2]
        if (float(soma) // 1 == soma):
            soma = int(soma)
        cubo = lista_todos[2]**3
        if (float(cubo) // 1 == cubo):
            cubo = int(cubo)
        produto = round(produto, 2)
        soma = round(soma, 2)
        cubo = round(cubo, 2)
        return print(f'''
        o produto do dobro do primeiro com metade do segundo: {produto}
        a soma do triplo do primeiro com o terceiro: {soma}
        o terceiro elevado ao cubo: {cubo}
        ''')


# numeros()


# IMC

''' Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 
IMC desejado (homens): (22 kg/m²)
IMC desejado (mulheres): (21 kg/m²)
Por exemplo, Renata pesa 85 kg e tem 1,76 m de altura.
PI = IMC desejado x (Altura x Altura)
PI = 21 x (1,76 x 1,76)
PI = 21 x 3,09
PI = 64,9 kg
O peso ideal para Renata é 64,9 kg.
''' # noqa


def peso_ideal():
    print("----------DESCUBRA SEU PESO IDEAL------------")
    sexo = input("Qual seu sexo: Feminino ou Masculino?(F/M)")
    altura = input("Qual sua altura em metros? ")
    peso = input("Qual seu peso em Kg? ")
    sexo = sexo.lower()
    imc_f = 21
    imc_h = 22

    def formula_peso_ideal(imc, altura) -> float():
        peso_ideal = float(imc) * float(float(altura)*float(altura))
        return float(peso_ideal)

    def porcentagem(peso_ideal, peso):
        peso_formatado = "{:.3f}".format(float(peso))
        if float(peso_ideal) > float(peso):
            porcentagem_peso = 100 - ((float(peso) / float(peso_ideal)) * 100)
            if float(porcentagem_peso) > 0.01:
                return (print(f'''Você esta {round(float(porcentagem_peso), 3)}% abaixo do peso ideal.
                  Seu peso: {peso_formatado}Kg
                  Sua altura: {round(float(altura), 2)}m
                  Peso ideal: {round(float(peso_ideal), 2)}Kg
                  '''))
            else:
                return (print(f'''Você está no peso ideal.
                  Seu peso: {peso_formatado}Kg
                  Sua altura: {round(float(altura), 2)}m
                  Peso ideal: {round(float(peso_ideal), 2)}Kg
                  '''))
        elif float(peso_ideal) < float(peso):
            porcentagem_peso = ((float(peso) / float(peso_ideal)) * 100) - 100
            if float(porcentagem_peso) > 0.01:
                return (print(f'''Você está {round(float(porcentagem_peso), 3)}% acima do peso ideal.
                    Seu peso: {peso_formatado}Kg
                    Sua altura: {round(float(altura), 2)}m
                    Peso ideal: {round(float(peso_ideal), 2)}Kg
                    '''))
            else:
                return (print(f'''Você está no peso ideal.
                  Seu peso: {peso_formatado}Kg
                  Sua altura: {round(float(altura), 2)}m
                  Peso ideal: {round(float(peso_ideal), 2)}Kg
                  '''))
        else:
            return (print(f'''Você esta no peso ideal.
                  Seu peso: {peso_formatado}Kg
                  Sua altura: {round(float(altura), 2)}m
                  Peso ideal: {round(float(peso_ideal), 2)}Kg
                  '''))

    if (bool(re.search(",", altura))) or (bool(re.search(",", peso))):
        altura_convertida = altura.replace(",", ".")
        peso_convertido = peso.replace(",", ".")
        altura = altura_convertida
        peso = peso_convertido
    else:
        altura = altura
        peso = peso
    if is_number(peso) and is_number(altura):
        if sexo == "feminino" or sexo == "f":
            peso_ideal = formula_peso_ideal(imc_f, altura)
            porcentagem(peso_ideal, peso)
        elif sexo == "masculino" or sexo == "m":
            peso_ideal = formula_peso_ideal(imc_h, altura)
            porcentagem(peso_ideal, peso)
        else:
            print("Sexo inválido.")
            print("--------------REINICIALIZANDO-------------\n")
            restart_program()
    else:
        print("Valores inválidos.")
        print("--------------REINICIALIZANDO--------------\n")
        restart_program()


# peso_ideal()


# programa que leia a variável peso (peso de peixes) e calcule o excesso
'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso
de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
a quantidade de quilos além do limite e na variável multa o valor da multa que
João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
''' # noqa


def multa_joao():
    peso_maximo = 50
    multa = 4.00
    deseja_adicionar = input("Deseja adicionar o peso de um peixe?(s/n)")
    deseja_adicionar = deseja_adicionar.lower()
    adicionar_mais_peixes = list([])
    valor_multa = list([])

    def calculando_multa_individual(peso, multa, peso_maximo):
        if (bool(re.search(",", peso))):
            peso_convertido = peso.replace(",", ".")
            peso = peso_convertido
        else:
            peso = peso
        if is_number(peso):
            if (float(peso) // 1 == peso):
                peso = int(peso)
            else:
                peso = round(float(peso), 3)
            if peso > peso_maximo:
                peso_restante = round((peso - peso_maximo), 3)
                total_multa = peso_restante*multa
                multa_formatada = "{:.2f}".format(float(total_multa))
                multa_formatada_string = str(multa_formatada.replace(".", ","))
                return f'''
                ---------------------PESO MÁXIMO ATINGIDO-----------------\n
                Peso do peixe pescado: {peso}Kg
                Peso máximo permitido: {peso_maximo}Kg
                Peso excedente do peixe pescado: {peso_restante}Kg
                Valor da multa em relação ao excedente pescado: R${multa_formatada_string} . 
                ''', float(multa_formatada) # noqa
            else:
                return f'''
                ----------------PESO PERMITIDO---------------------\n
                Peso do peixe pescado: {peso}Kg
                Peso máximo permitido: {peso_maximo}Kg
                Peso excedente do peixe pescado: 0Kg
                Valor da multa em relação ao excedente pescado: R$ 0. 
                ''' # noqa
        else:
            print("Valor inválido")
            print("--------------REINICIALIZANDO--------------\n")
            restart_program()

    if deseja_adicionar == "sim" or deseja_adicionar == "s":
        def verificar_tipo_retorno(resultado):
            if isinstance(resultado, tuple):
                return True
            else:
                return False
        peso = input("Digite o peso do peixe em Kg: ")
        resultado = calculando_multa_individual(peso, multa, peso_maximo)
        if verificar_tipo_retorno(resultado):
            print(resultado[0])
            valor_multa.append(resultado[1])
        else:
            print(resultado)
        if float(peso) > peso_maximo:
            adicionar_mais_peixes.append(float(peso))
        adicionar_mais = input("Deseja adicionar mais peixes?(s/n) ")
        if adicionar_mais == "sim" or adicionar_mais == "s":
            adicionar_mais = bool(True)
            while adicionar_mais:
                peso = input("Digite o peso do peixe em Kg: ")
                resultado = calculando_multa_individual(peso, multa, peso_maximo) # noqa
                if verificar_tipo_retorno(resultado):
                    print(resultado[0])
                    valor_multa.append(resultado[1])
                else:
                    print(resultado)
                if float(peso) > peso_maximo:
                    adicionar_mais_peixes.append(float(peso))
                adicionar_mais = input("Deseja adicionar mais peixes?(s/n) ")
                if adicionar_mais == "sim" or adicionar_mais == "s":
                    adicionar_mais = bool(True)
                else:
                    soma_multa = sum(valor_multa)
                    print('''
                -------TODOS OS PEIXES QUE HOUVE APLICAÇÃO DE MULTA-------
                    ''')
                    for (peixe, multa) in zip(adicionar_mais_peixes, valor_multa): # noqa
                        print(f'''
                              ---------Peixe----------
                              Peso do peixe: {peixe} Kg
                              Valor multa: R${multa}
                              ''')
                    print(f'''
                            VALOR TOTAL DA MULTA: R$ {soma_multa}
                        ''')
                    print("--------------------ENCERRANDO-----------------")
                    break
        else:
            print("Encerrando")


# multa_joao()
