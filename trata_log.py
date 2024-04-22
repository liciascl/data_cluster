import csv

# Caminho para o arquivo .log
log_file_path = 'slurm_jobcomp.log'

# Caminho para o arquivo .csv de saída
csv_file_path = 'output.csv'

# Lista para armazenar os dados
data = []

# Ler o arquivo .log
with open(log_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line:  # Verificar se a linha não está vazia
            # Dividir a linha em pares chave-valor
            entry = {}
            pairs = line.split()
            for pair in pairs:
                key, value = pair.split('=', 1)
                entry[key] = value
            data.append(entry)

# Campos que serão escritos no arquivo CSV
fieldnames = ['JobId', 'UserId', 'GroupId', 'Name', 'JobState', 'Partition', 
              'TimeLimit', 'StartTime', 'EndTime', 'NodeList', 'NodeCnt', 
              'ProcCnt', 'WorkDir', 'ReservationName', 'Tres', 'Account', 'QOS', 
              'WcKey', 'Cluster', 'SubmitTime', 'EligibleTime', 'DerivedExitCode', 'ExitCode']

# Criar e escrever no arquivo CSV
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        # Assegurar que todas as chaves estejam presentes na linha, mesmo se algumas estiverem ausentes
        row_sanitized = {key: row.get(key, '') for key in fieldnames}
        writer.writerow(row_sanitized)

print('CSV file has been created successfully.')

