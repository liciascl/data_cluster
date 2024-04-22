import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
csv_file_path = 'output.csv'
data = pd.read_csv(csv_file_path)

# Excluir usuários especificados
usuarios_para_excluir = ['licia', 'root', 'michel']
data = data[~data['UserId'].isin(usuarios_para_excluir)]

# Limpar e preparar dados
data['SubmitTime'] = pd.to_datetime(data['SubmitTime'], errors='coerce')
data['EndTime'] = pd.to_datetime(data['EndTime'], errors='coerce')
data['StartTime'] = pd.to_datetime(data['StartTime'], errors='coerce')
data['Duration'] = (data['EndTime'] - data['StartTime']).dt.total_seconds() / 60  # Duração em minutos

# Análise de submissões por usuário
submission_counts = data['UserId'].value_counts()
print("Submissões por usuário:")
print(submission_counts)

# Plot: Submissões por usuário
plt.figure(figsize=(10, 6))
submission_counts.plot(kind='bar', color='blue')
plt.title('Submissões por Usuário')
plt.xlabel('Usuário')
plt.ylabel('Número de Jobs Submetidos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('imgs/submissions_by_user.png')
plt.show()

# Análise do estado dos jobs
job_states = data['JobState'].value_counts()
print("Contagem de estados dos jobs:")
print(job_states)

# Plot: Estados dos Jobs
plt.figure(figsize=(10, 6))
job_states.plot(kind='pie', autopct='%1.1f%%')
plt.title('Estados dos Jobs')
plt.ylabel('')
plt.tight_layout()
plt.savefig('imgs/job_states_distribution.png')
plt.show()

# Análise da quantidade de recursos alocados por job (exemplo com memória)
data['Mem'] = data['Tres'].apply(lambda x: int(x.split(',')[1].split('=')[1].replace('G', '').replace('M', '')) if 'mem' in x else 0)
plt.figure(figsize=(10, 6))
data['Mem'].plot(kind='hist', bins=20, color='green')
plt.title('Memória Alocada por Job')
plt.xlabel('Memória (G)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('imgs/memory_allocation_histogram.png')
plt.show()

# Análise da duração dos jobs
print("Duração dos jobs (minutos):")
print(data['Duration'].describe())

# Plot: Duração dos Jobs
plt.figure(figsize=(10, 6))
data['Duration'].plot(kind='hist', bins=30, color='purple')
plt.title('Distribuição da Duração dos Jobs')
plt.xlabel('Duração (Minutos)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('imgs/job_duration_histogram.png')
plt.show()
