# 1) Digite este exemplo em um script e teste-o.
def do_twice(f):
    f()
    f()

def print_spam():
    print('SPAM')

do_twice(print_spam)


# 2) Altere do_twice para que receba dois argumentos, um objeto de função e um valor, 
# e chame a função duas vezes, passando o valor como um argumento.
def do_twice(funcao, argumento):
    funcao(argumento)
    funcao(argumento)


# 3) Copie a definição de print_twice que aparece anteriormente neste capítulo para 
# seu script.
def print_twice(monty):
    print(monty)
    print(monty)


# 4) Use a versão alterada de do_twice para chamar print_twice duas vezes, passando 
# 'spam' como um argumento.

do_twice(print_twice, 'Spam!')


# 5) Defina uma função nova chama do_four que receba um objeto de função e um valor
# e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver apenas
# duas declarações (afirmações) no corpo desta função, não quatro.
def do_four(print_twice, valor):
    print_twice(valor)
    print_twice(valor)

do_four(print_twice, '4 vezes')