# EX 1

while True:
    try:
        lista = []

        for i in range(0,2):
            valor = float(input(f"Digite um valor para a posição {i}: "))
            lista.append(valor)
        
        dividendo = int(input("\nDigite a posição do número para ser o dividendo: "))
        divisor = int(input("\nDigite a posição do número para ser o divisor: "))

        resultado = lista[dividendo] / lista[divisor]

    except ValueError:
        print("O valor digitado é invalido.")

    except ZeroDivisionError:
        print("Não é possível dividir por 0.")

    except IndexError:
        print("Uma das posições digitadas não existe.")

    except KeyboardInterrupt:
        print("Programa interrompido.")
        break

    else:
        print(f"\nO resultado da divisão é: {resultado}.")
        break
