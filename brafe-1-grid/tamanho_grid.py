"""
    GRID EM PORCENTAGEM
    Fórmula: 100% / colunas * grid
"""

# Qtd de colunas em seu grid ---> colunas
# 100% -------------------------> cem
# tamanho em pixels do gutter --> gutter

cem = 100
colunas   = 12
grid      = 1
gutter = 20

for grid in range(1, colunas+1):
    result = cem / colunas * grid
       
    result_string = str(result)
    lista = result_string.split('.')
    
    inteira = lista[0]
    decimal = lista[1]
    
    if int(decimal) == 0:
        porcentagem_final = inteira
        print(f'.grid-{grid}', end=' ')
        print('{width: calc('+porcentagem_final+'% - '+str(gutter)+'px)}')
    else:
        porcentagem_final = inteira + '.' + decimal[:3]
        print(f'.grid-{grid}', end=' ')
        print('{width: calc('+porcentagem_final+'% - '+str(gutter)+'px)}')


print()


