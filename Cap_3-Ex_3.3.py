# 1) Escreva uma função que desenhe uma grade como a seguinte:
def desenha_aresta(arestas) -> int:
    print('+ - - - - ' *arestas, end= "+\n")

def desenha_coluna(colunas) -> int:
    print('|         ' *colunas, end = '|\n')

def do_twice(func, arg):
    func(arg)
    func(arg)

def do_four(func, arg):
    do_twice(func,arg)
    do_twice(func,arg)

def quadrante(n):
    desenha_aresta(n)
    do_four(desenha_coluna, n)

def quadrante_final(n):
    do_twice(quadrante, n)
    desenha_aresta(n)

quadrante_final(2)
print('\n')

# 2) Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.
def print_grid():
    cont = 3
    while cont >= 0:
        if cont == 0:
            desenha_aresta(3)
            break
        else:
            desenha_aresta(3)
            do_four(desenha_coluna, 3)
            cont -= 1


print_grid()
