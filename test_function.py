def calcular_imc(peso, altura):

    imc = peso / (altura ** 2)

    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

#O GRAFO DA FUNÇÃO ESTÁ EM GRAFE.TXT
#Calculo para a complexidade ciclomática:

# A - ARESTAS
# N - NÓS
# C - CONEXÕES
# SÃO 6 ARESTAS, 5 NÓS E UM COMPONENTE


# V(G) - COMPLEXIDADE CICLOMÁTICA
# V(G) = A - N + 2*C
# V(G) = 6 - 5 + 2 * 1 = 3

# SÃO 5 ARESTAS, 4 NÓS E UM COMPONENTE ÚNICO