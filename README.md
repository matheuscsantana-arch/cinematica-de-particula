# 🏎️ Cinemática de Partícula

Este é um projeto desenvolvido em Python voltado para o estudo da cinemática escalar. O software recebe uma equação polinomial de posição $s(t)$, realiza derivações simbólicas para encontrar as equações de velocidade $v(t)$ e aceleração $a(t)$, e gera gráficos da posição, velocidade e aceleração para análise do movimento em um intervalo de tempo.

## 💻 Tecnologias

- Python 3.10+.
- Bibliotecas `numpy`, `matplotlib`, `sympy`

## ⚙️ Instalação
1. Certifique-se de ter o Python e as bibliotecas necessárias instaladas:

```bash
pip install -r requirements.txt
```

2. Baixe o arquivo cinematica_de_particula.py.
3. Execute o programa:

```bash
python cinematica_de_particula.py
```
## 🛠️ Funcionalidades

| Recurso | Descrição | Detalhes |
| :--- | :--- | :--- |
| **Cálculo Simbólico** | Calcula as derivadas de $s(t)$ para obter $v(t)$ e $a(t)$. | Utiliza a biblioteca `sympy` para derivação exata. |
| **Entrada Polinomial** | Permite definir dinamicamente o grau e os coeficientes. | Suporta polinômios de qualquer ordem (grau $n$). |
| **Vetorização Numérica** | Converte as funções simbólicas em dados processáveis. | Integra `lambdify` do SymPy com vetores `numpy`. |
| **Visualização Gráfica** | Gera gráficos de posição, velocidade e aceleração. | Utiliza `matplotlib` para plotagem simultânea. |

## 🕹️ Como usar

1. Inicie o programa e digite n para começar a entrada de dados.
2. Informe o grau do polinômio (ex: 2 para uma função quadrática).
3. Insira os coeficientes para cada termo (ex: $t^2, t$ e termo constante).
4. O programa exibirá as equações resultantes no console.
5. Uma janela com os gráficos de Posição ($m$), Velocidade ($m/s$) e Aceleração ($m/s^2$) será aberta para análise.

## 💡 Exemplo de uso

- O programa vai perguntar ao usuário se ele deseja encerrar o programa.
- Ao digitar "n" o programa irá pedir o grau do polinômio e seus coeficientes.
- Inserindo 2 para o grau, 5 para o primeiro coeficiente, 2 para o segundo coeficiente e 10 para o último coeficiente:

<p align="left">
  <img src="assets/polinomio.PNG" alt="Polinômio de entrada" >
</p>

- O programa calcula e exibe as equações do movimento:

<p align="left">
  <img src="assets/equacoes.PNG" alt="Equações do movimento" >
</p>

- Em seguida plota os gráficos:
- s(t)
<p align="left">
  <img src="assets/grafico_pos.PNG" alt="Gráfico da posição" width="400">
</p>

- v(t)
<p align="left">
  <img src="assets/grafico_vel.PNG" alt="Gráfico da velocidade" width="400">
</p>

- a(t)
<p align="left">
  <img src="assets/grafico_acel.PNG" alt="Gráfico da aceleração" width="400">
</p>

- Após fechar os gráficos, o programa pergunta ao usuário se ele deseja encerrar o programa:

<p align="left">
  <img src="assets/loop.PNG" alt="Loop iterativo" >
</p>

## 🚀 Status do Projeto

✅ Concluído

## 👤 Autor

Feito por **Matheus Felipe Claudino de Santana**  
GitHub: https://github.com/matheuscsantana-arch
