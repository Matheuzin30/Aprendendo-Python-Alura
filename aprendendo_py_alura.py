# -*- coding: utf-8 -*-
"""Aprendendo PY ALura.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Es8hvBtoOL9uyQD7v-rHrvRWwVjxWxvy
"""



import requests
req = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(req)
data = resposta.json()
data[1]

import random

valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']
print(f'Apalavra secreta tem {len(palavra_secreta)} letras -> {dica}')

chute == input(f'A dica é -> {dica} ')
if chute == palavra_secreta:
  print('Acertou')
else:
    print(f'Errou! a palavra secreta era "{palavra_secreta}".')