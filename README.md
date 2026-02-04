# 🏎️ Cinemática de Partícula

Este é um projeto desenvolvido em Python voltado para o estudo da cinemática escalar. O software recebe uma equação polinomial de posição $s(t)$, realiza derivações simbólicas para encontrar as equações de velocidade $v(t)$ e aceleração $a(t)$, e gera gráficos da posição, velocidade e aceleração para análise do movimento em um intervalo de tempo.

## 💻 Tecnologias

- Python 3.10+.
- Bibliotecas `numpy`, `matplotlib`, `sympy`

## ⚙️ Instalação
1. Certifique-se de ter o Python e as bibliotecas necessárias instaladas:

```bash
pip install numpy matplotlib sympy
```

2. Baixe o arquivo Cinematica_de_particula.py.
3. Execute o programa:

```bash
python Cinematica_de_particula.py
```
## 🛠️ Funcionalidades

| Recurso | Descrição | Detalhes |
| :--- | :--- | :--- |
| **Cálculo Simbólico** | Calcula as derivadas de $s(t)$ para obter $v(t)$ e $a(t)$. | Utiliza a biblioteca `sympy` para derivação exata. |
| **Entrada Polinomial** | Permite definir dinamicamente o grau e os coeficientes. | Suporta polinômios de qualquer ordem (grau $n$). |
| **Vetorização Numérica** | Converte as funções simbólicas em dados processáveis. | Integra `lambdify` do SymPy com vetores `numpy`. |
| **Visualização Gráfica** | Gera gráficos de posição, velocidade e aceleração. | Utiliza `matplotlib` para plotagem simultânea. |

## 🕹️ Como usar

1. Inicie o programa e escolha [n] para começar a entrada de dados.
2. Informe o grau do polinômio (ex: 2 para uma função quadrática).
3. Insira os coeficientes para cada termo (ex: $t^2, t$ e termo constante).
4. O programa exibirá as equações resultantes no console.
5. Uma janela com os gráficos de Posição ($m$), Velocidade ($m/s$) e Aceleração ($m/s^2$) será aberta para análise.

## 💡 Exemplo de uso

Ao inserir um polinômio de grau 2 com coeficientes para $s(t) = 5t^2 + 2t + 10$:
s(t) = 5t**2 + 2t + 10
v(t) = 10*t + 2
a(t) = 10O 
programa então plota as curvas de crescimento parabólico, linear e a aceleração constante.

## 🚀 Status do Projeto

✅ Concluído

## 👤 Autor

Feito por **Matheus Felipe Claudino de Santana**  
GitHub: https://github.com/matheuscsantana-arch
