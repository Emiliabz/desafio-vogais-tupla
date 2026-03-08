"""
DESAFIO: Contando Vogais em Tupla
-------------------------------------------------------------------------
Enunciado:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Destaques:
- Uso de laços aninhados (for dentro de for).
- Verificação de caracteres usando o operador 'in'.
- Manipulação de strings (.upper() e .lower()).
-------------------------------------------------------------------------
"""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalho', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos as vogais: ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[31m{letra}\033[m', end=' ')

print('\n' + '-' * 40)