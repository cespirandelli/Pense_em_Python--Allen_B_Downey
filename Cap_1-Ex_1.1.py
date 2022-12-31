# 1) Em uma insttrução print, o que acontece se você omitir um dos parênteses ou ambos?

#### print"Hello World") # SyntaxError: invalid syntax
#### print("Hello World" #SyntaxError: unexpected EOF while parsing
#### print"Hello World" # SyntaxError: invalid syntax
print("Hello World !")

# 2) Se você estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?

#### print(ex) # NameError: name 'ex' is not defined
#### print("ex) # SyntaxError: EOL while scanning string literal
#### print("x') # SyntaxError: EOL while scanning string literal
print("ex")

# 3) Você pode usar um sinal de menos para fazer um número negativo como -2. 
# O que acontece se colocar um sinal de mais antes de um número? E se colocar dois sinais de mais '++'?

#### print(2+) SyntaxError: invalid syntax
print(++2) # 2


# 4) Na notação matemática, zeros à esquerda são aceitáveis, como em 02. 
# O que acontece se você tentar usar isso em Python?

#### print(02) # SyntaxError: leading zeros in decimal integer literals are not permitted; 
               # use an 0o prefix for octal integers
               # SyntaxError: invalid token
print(0o3) # 3

# 5) O que acontece se você tiver dois valores sem nenhum operador entre eles?

#### print(2 3) # SyntaxError: invalid syntax
print(4+3)