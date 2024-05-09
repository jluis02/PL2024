import fileinput
import re

stdin = "\n".join(fileinput.input())

simbolos_contas = r'(on|off|=|\d+)'
symbols = re.findall(simbolos_contas, stdin, flags=re.IGNORECASE)

somador = True
current = 0

for symbol in symbols:
    if symbol.lower() == 'on':
        somador = True
    elif symbol.lower() == 'off':
        somador = False
    elif symbol.isdigit() and somador:
        current += int(symbol)
    elif symbol == '=':
        print(f'Soma: {current}')