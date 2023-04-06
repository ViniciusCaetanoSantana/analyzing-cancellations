import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')

tabela = tabela.drop('Unnamed: 0', axis=1)

tabela = tabela.drop('IDCliente', axis=1)

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

tabela = tabela.dropna(axis=1, how='all')

tabela = tabela.dropna(axis=0, how='any')

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()
