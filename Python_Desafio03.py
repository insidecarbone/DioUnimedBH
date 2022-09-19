#Desafio 03 - Cálculo de viagem

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()

tempo_viagem = int(valores[0])
velocidade = int(valores[1])

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

resultado = float(tempo_viagem*velocidade)/12

print(f'{resultado:.3f}')