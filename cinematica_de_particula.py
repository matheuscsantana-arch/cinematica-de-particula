# Bibliotecas
import numpy as np
import matplotlib.pyplot as grafico
import sympy as sp

# Funções
def calcular_posicao(s,t,tempo):
    # Transformando a equação simbólica em equação numérica
    s_f = sp.lambdify(t, s, 'numpy')

    # Calculando o vetor posição
    posicao = s_f(tempo) + np.zeros_like(tempo)
    return posicao

def calcular_velocidade(v,t,tempo):
    # Transformando a equação simbólica em equação numérica
    v_f = sp.lambdify(t, v, 'numpy')

    # Calculando o vetor velocidade
    velocidade = v_f(tempo) + np.zeros_like(tempo)
    return velocidade

def calcular_aceleracao(a,t,tempo):
    # Transformando a equação simbólica em equação numérica
    a_f = sp.lambdify(t, a, 'numpy')

    # Calculando o vetor aceleração
    aceleracao = a_f(tempo) + np.zeros_like(tempo)
    return aceleracao

def plotar_grafico(x, y, cor_linha, titulo, eixo_x, eixo_y):
    # x - vetor do eixo x
    # y - vetor do eixo y
    # outros - strings para costumizar o gráfico

    grafico.figure()
    grafico.plot(x, y, color = cor_linha)
    grafico.title(titulo)
    grafico.xlabel(eixo_x)
    grafico.ylabel(eixo_y)
    grafico.grid(True)

# Início do programa

encerrar = False
while not encerrar:
    
    escolha = input("Você deseja finalizar o programa? [s]im ou [n]ão ")
    escolha = escolha.lower()

    if escolha == "s":
        encerrar = True
        continue
    
    try:
        grau = input("Informe o grau do polinômio: ")
        grau = int(grau)

        if grau >= 0:
            
            coeficientes = np.zeros(grau+1)
            t = sp.symbols('t')
            j = grau
        
        else:
            print("Digite apenas inteiros positivos")
            continue

    except ValueError:
        print("Digite apenas números inteiros")
        continue
    
    try:
        # Coletando os coeficientes
        for i,valor in enumerate(coeficientes):
            
            if j >= 2:
                coeficientes[i] = input(f'Digite o coeficiente de t^{j}: ')
                coeficientes[i] = float(coeficientes[i])
                j -= 1

            elif j == 1:
                coeficientes[i] = input(f'Digite o coeficiente de t: ')
                coeficientes[i] = float(coeficientes[i])
                j -= 1

            elif j == 0:
                coeficientes[i] = input(f'Digite o último termo: ')
                coeficientes[i] = float(coeficientes[i])
                j -= 1

    except ValueError:
        print("Valor inválido!")
        continue
    
    # Gerando a equação da posição
    s = 0
    j = grau
    for i in coeficientes:
        s += i*t**(j)
        j -= 1

    # Equação simbólica da velocidade
    v = sp.diff(s,t)

    # Equação simbólica da aceleração
    a = sp.diff(v,t)

    # Mostrando as equações na tela
    print(f's(t) = {s}')
    print(f'v(t) = {v}')
    print(f'a(t) = {a}')

    # Criando o vetor tempo com 101 elementos de 0 a 10 segundos
    tempo = np.linspace(0,10,101)

    # Calculando os vetores posição, velocidade e aceleração
    posicao = calcular_posicao(s,t,tempo)
    velocidade = calcular_velocidade(v,t,tempo)
    aceleracao = calcular_aceleracao(a,t,tempo)

    # Plotando s(t), v(t) e a(t)
    plotar_grafico(tempo, posicao, 'red', "Posição x Tempo", "t [s]", "s [m]")
    plotar_grafico(tempo, velocidade, 'black', "Velocidade x Tempo", "t [s]", "v [m/s]")
    plotar_grafico(tempo, aceleracao, 'blue', "Aceleração x Tempo", "t [s]", "a [m/s²]")
    grafico.show()
    grafico.close()
