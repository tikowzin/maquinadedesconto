print('////////MAQUINA DE DESCONTO///////')
print('     ')
print('     ')

preco = float(input('QUAL O PREÇO DO PRODUTO?'))
desconto = float(input('QUANTOS % DE DESCONTO?'))

total = preco - (preco * desconto / 100)
print('O produto custava R$', preco, 'com desconto de', desconto,'%', 'vai custar' ,total ,'R$')

print('     ')
print('     ')

print('FIM')


