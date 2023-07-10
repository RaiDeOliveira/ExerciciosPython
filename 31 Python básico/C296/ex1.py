# EX 1

# Recebe o valor da temperatura em graus Celcius e a armazena na variável "celcius"
# Retorna o valor da variável "celcius"
def lerTemperatura():
    celcius = float(input("Insira o valor da temperatura em graus Celcius: "))
    return(celcius)


# Recebe o parâmetro "c", que representa o valor da temperatura em graus Celcius
# Converte o valor de "c" para Fahrenheit e armazena o resultado na variável "fahrenheit"
# Retorna o valor da variável "fahrenheit"
def converterTemperatura(c):
    fahrenheit = (c * 9 + 160) / 5
    return(fahrenheit)


# Recebe o parâmetro "f", que representa a temperatura em Fahrenheit
# Imprime a mensagem junto ao valor de "f"
def exibirTemperatura(f):
    print(f"O valor dessa temperatura em Fahrenheit é igual a {f}")

# "lerTemperatura()" recebe e retorna o valor da temperatura em graus Celcius
# "converterTemperatura()" recebe o valor retornado por "lerTemperatura()" e retorna-o convertido em Fahrenheit
# "exibirTemperatura()" imprime o valor retornado por "converterTemperatura()"
exibirTemperatura(converterTemperatura(lerTemperatura()))