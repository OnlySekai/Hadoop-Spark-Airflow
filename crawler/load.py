import csv
import subprocess

from constants import NAME_NODE_ID

def write_to_hdfs(filename, trx):
    if len(trx):
        local_path = f'../hadoop_namenode/{filename}'
        with open(local_path, 'w', newline='') as csvfile:
            fieldnames = list(trx[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in trx:
                writer.writerow(transaction)
        command = f'docker exec {NAME_NODE_ID} hdfs dfs -put -f /hadoop/dfs/name/{filename} /'
        subprocess.run(command.split(' '))
        subprocess.run(f'rm {local_path}'.split(' '))
