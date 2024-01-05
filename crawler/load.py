import pandas as pd
import subprocess

from constants import NAME_NODE_ID

def write_to_hdfs(filename, trx):
    if len(trx):
        local_path = f'../hadoop_namenode/{filename}'
        pd.DataFrame(trx).to_csv(local_path, index=False)
        command = f'docker exec {NAME_NODE_ID} hdfs dfs -put -f /hadoop/dfs/name/{filename} /'
        subprocess.run(command.split(' '))
        subprocess.run(f'rm {local_path}'.split(' '))
