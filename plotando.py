import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados do arquivo CSV
csv_file_path = 'output_tratado.csv'
data = pd.read_csv(csv_file_path)

# Processar o campo UserId para extrair apenas o nome do usuário antes dos parênteses
data['UserId'] = data['UserId'].apply(lambda x: x.split('(')[0])

# Excluir usuários específicos
users_to_exclude = ['licia', 'root', 'michel']
data = data[~data['UserId'].isin(users_to_exclude)]


# Converter SubmitTime para datetime para facilitar a plotagem
data['SubmitTime'] = pd.to_datetime(data['SubmitTime'], errors='coerce')

# Gráfico 1: Histograma dos Estados dos Jobs
plt.figure(figsize=(10, 6))
data['JobState'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Estados dos Jobs')
plt.xlabel('Estado do Job')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('imgs/job_states_histogram.png')
plt.show()

# Gráfico 2: Gráfico de Barras do Contador de Nós
plt.figure(figsize=(10, 6))
data['NodeCnt'].value_counts().sort_index().plot(kind='bar', color='green')
plt.title('Distribuição de Jobs por Nós')
plt.xlabel('Número de Nós')
plt.ylabel('Número de Jobs')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('imgs/node_count_bar_chart.png')
plt.show()

# Gráfico 3: Gráfico de Linhas do Tempo de Submissão
plt.figure(figsize=(12, 7))
data['SubmitTime'].dt.floor('d').value_counts().sort_index().plot(kind='line', marker='o', linestyle='-')
plt.title('Jobs Submetidos ao Longo do Tempo')
plt.xlabel('Data de Submissão')
plt.ylabel('Número de Jobs')
plt.grid(True)
plt.tight_layout()
plt.savefig('imgs/submission_time_line_chart.png')
plt.show()
