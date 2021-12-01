n = int(input())
lista = list(map(int, input().split()))
a=min(lista)
c=lista.index(a)
print("Menor valor: {}".format(a))
print("Posicao: {}".format(c))

    