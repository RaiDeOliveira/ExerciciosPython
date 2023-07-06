# EX 2

kmsLitro = 12

def lerValores():
    velMedia = float(input("Insira a velocidade média de sua viagem em km/h: "))
    tempoGasto = float(input("Insira o tempo gasto na sua viagem em horas: "))
    return(velMedia, tempoGasto)

def calcDistancia(val):
    distancia = val[0] * val[1]
    return distancia

def calcLitros(dis):
    litros = dis / kmsLitro
    return litros


def exibeResultado(v, t, d, l):
    print("\nVelocidade média: {}km/h \nTempo gasto: {}h \nDistância percorrida: {}km \nCombustível gasto: {}L".format(v, t, d, l))

val = lerValores()
dis = calcDistancia(val)
lit = calcLitros(dis)

exibeResultado(val[0], val[1], dis, lit)
