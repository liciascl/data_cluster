import re
from datetime import datetime

# Definir o caminho do arquivo de log
log_path = 'slurmctld.log'

# Padrões Regex para capturar informações relevantes
job_pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3})\] .*?JobId=(\d+) .*?(CANCELED|FAILED|TIMEOUT)')
error_pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3})\] error: (.*)')

## Converter strings de data/hora em objetos datetime
def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")

# Listas para armazenar dados
jobs = []
errors = []

# Ler o arquivo e extrair informações
with open(log_path, 'r') as file:
    for line in file:
        job_match = job_pattern.search(line)
        if job_match:
            timestamp, job_id, status = job_match.groups()
            jobs.append({'job_id': job_id, 'timestamp': timestamp, 'status': status})
            print(f"Captured Job - ID: {job_id}, Time: {timestamp}, Status: {status}")

        error_match = error_pattern.search(line)
        if error_match:
            timestamp, message = error_match.groups()
            errors.append({'timestamp': timestamp, 'message': message})
            print(f"Captured Error - Time: {timestamp}, Message: {message}")
