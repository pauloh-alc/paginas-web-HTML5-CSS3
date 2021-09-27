
# Tamanho do container       ---> container
# Qtd de colunas em seu grid ---> colunas
# grid específico            ---> grid
# gutter                     ---> distância entre um grid para outro


# @media only screen and (min-width: 768px) and (max-width: 959px)
container = 768
colunas   = 16
grid      = 1
gutter    = 20


for grid in range(1, 17):
    result = (container / colunas * grid) - gutter
    print('.grid-'+str(grid)+' {width: '+str(result)+'px;}')


grid = 16/3

result = (container / colunas * grid) - gutter
print('.grid-1-3 {width: '+str(result)+'px;}')

print()

# @media only screen and (max-width: 767px)

container = 300
colunas   = 16
grid      = 1
gutter    = 0


for grid in range(1, 17):
    result = (container / colunas * grid) - gutter
    print('.grid-'+str(grid)+' {width: '+str(result)+'px;}')


grid = 16/3

result = (container / colunas * grid) - gutter
print('.grid-1-3 {width: '+str(result)+'px;}')
