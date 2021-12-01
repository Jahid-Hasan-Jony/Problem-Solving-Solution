entrada = input().split()
altura_pulo = int(entrada[0])

canos = [int(c) for c in input().split()]

resultado = "YOU WIN"
for i in range(len(canos) - 1):

    diferenca = abs(canos[i+1] - canos[i])

    if diferenca > altura_pulo:
        resultado = "GAME OVER"
        break

print(resultado)