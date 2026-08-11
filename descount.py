print('////////MAQUINA DE DESCONTO///////')
print('     ')
print('     ')

while True:
    try:
        preco = float(input('QUAL O PREÇO DO PRODUTO? '))
        desconto = float(input('QUANTOS % DE DESCONTO? '))


        if preco < 0 or desconto < 0 or desconto > 100:
            print('Valores inválidos! Preço não pode ser negativo e desconto deve estar entre 0 e 100.')
            print('     ')
            continue

        total = preco - (preco * desconto / 100)
        print('O produto custava R$', preco, 'com desconto de', desconto, '%', 'vai custar', total, 'R$')
        break

    except ValueError:
        print('Entrada inválida! Digite apenas números (use ponto para decimais, ex: 10.50).')
        print('     ')

print('     ')
print('     ')

print('FIM')
