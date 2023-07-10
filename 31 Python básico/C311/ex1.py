# EX 1

import re

texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 ou 11111-111. Meu site é https://www.iaexpert.academy ou http://iaexpert.com.br"

numeros = re.findall('\d', texto)

ceps = re.findall('\d{5,5}-\d{3,3}', texto)

sites = re.findall('https?://[A-Za-z0-9.]+', texto)

print(f"Numeros: {numeros}\nCEPs: {ceps}\nSites: {sites}")