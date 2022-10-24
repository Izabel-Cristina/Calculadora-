while True:
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    if numero_1.isnumeric() and numero_2.isnumeric():
        print(numero_1)
        print(numero_2)
        break
    else: 
        print('Digite apenas numero: ')

operacao = input('''Digite uma operação:
 + para adição.
 - para subtração.
 * para multiplicação.
 / para divisão.
 ** para potenciação
''')

if operacao =='+':
    resultado = int(numero_1) + int(numero_2)
    print('{} + {} = '.format(numero_1, numero_2,))
    print (resultado)

elif operacao == '-':
    resultado = int(numero_1) - int(numero_2)
    print('{} - {} = '.format(numero_1, numero_2,))
    print (resultado)
    
elif operacao == '*':
    resultado = int(numero_1) * int(numero_2)
    print('{} * {} = '.format(numero_1, numero_2,))
    print (resultado)
    
elif operacao == '/':
    resultado = int(numero_1) / int(numero_2)
    print('{} / {} = '.format(numero_1, numero_2,))
    print (resultado)
    
elif operacao == '**':
    resultado = int(numero_1) ** int(numero_2)
    print('{} ** {} = '.format(numero_1, numero_2,))
    print (resultado)
    
else:
    print('Escolha uma operação válida')
