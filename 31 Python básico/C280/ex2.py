# EX 2

print('Boas vindas ao sistema de cálculo para viagens com seu automóvel!\n')

tempoGasto = float(input('Insira o tempo que você gastou na viagem (em horas): '))
velocidadeMedia = float(input('\nInsira a velocidade média de sua viagem (em km/h): '))

distanciaPercorrida = velocidadeMedia * tempoGasto
quantidadeCombustivel = round(distanciaPercorrida / 12, 3)

print(f'\nVocê percorreu {distanciaPercorrida}km e gastou {quantidadeCombustivel} litros de combustível.')
