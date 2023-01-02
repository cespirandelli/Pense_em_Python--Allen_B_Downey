def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# Nem sempre se deve ler um programa de cima para baixo. Às vezes, é mais útil
# começar no meio e ler para cima e para baixo. Por exemplo, para encontrar o
# erro em um programa, você pode querer começar no ponto onde o programa
# falha e procurar para trás. Às vezes, o ponto onde o programa falha é
# antes do ponto onde você começou a procurar.

def print_twice(bruce):
    print(bruce)
    print(bruce)

# Quando você cria uma variável dentro de uma função, ela é local, ou seja, ela só
# existe dentro da função. Por exemplo:

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

# Esta função recebe dois argumentos, concatena-os e exibe o resultado duas vezes.
# Se você tentar usar cat fora da função, você recebe um erro: "cat" não existe,
# porque cat é local a cat_twice.
# print(cat) #NameError: name 'cat' is not defined

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)