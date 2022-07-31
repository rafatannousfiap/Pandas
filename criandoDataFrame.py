## Importando o pandas
import pandas as pd

## Definindo pessoas a partir de um dicionário
pessoas = {
    'nome': ['Rafael', 'Ciclano', 'Beltrano'],
    'idade': ['20', '30', '40']
}

## Criando o dataframe
df = pd.DataFrame(pessoas)

## Imprimindo ele
print(df)