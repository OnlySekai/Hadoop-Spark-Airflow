from concurrent.futures import ThreadPoolExecutor
from web3_util import web3Util
from db import load_db, save_db
from extract import extract_transactions, extract_blocks, extract_withdrawals
from load import write_to_hdfs

print('start crawler')
last_block, block_step = load_db()

with ThreadPoolExecutor() as executor:
    blocks = list(executor.map(web3Util.get_block, range(
        last_block, last_block + block_step)))
label = ['transaction', 'withdrawal', 'block']
if len(blocks):
    for index, function in enumerate([extract_transactions, extract_withdrawals, extract_blocks]):
        data = function(blocks)
        filename = f'{label[index]}-{last_block}.csv'
        write_to_hdfs(filename, data)
    save_db(last_block+block_step, 100)
else:
    print('No new blocks')
