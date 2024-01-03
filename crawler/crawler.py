from concurrent.futures import ThreadPoolExecutor
from web3_util import web3Util
from db import load_db, save_db
from extract import extract_transactions
from load import write_to_hdfs

last_block, block_step = load_db()

with ThreadPoolExecutor() as executor:
    blocks = list(executor.map(web3Util.get_block, range(
        last_block, last_block + block_step)))

trx = extract_transactions(blocks)
filename = f'transaction-{last_block}.csv'
write_to_hdfs(filename, trx)
save_db(last_block+block_step)
