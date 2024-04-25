
def check_number(number_input):
    if number_input % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

number_input = int(input("Who is number? "))
check_number(number_input)

#O GRAFO DA FUNÇÃO ESTÁ EM GRAFE.TXT
#Calculo para a complexidade ciclomática:

# A - ARESTAS
# N - NÓS
# C - CONEXÕES
# SÃO 5 ARESTAS, 4 NÓS E UM COMPONENTE ÚNICO


# V(G) - COMPLEXIDDE CICLOMÁTICA
# V(G) = A - N + 2*C
# V(G) = 5 - 4 + 2 * 1 = 3

# SÃO 5 ARESTAS, 4 NÓS E UM COMPONENTE ÚNICO