def extract_transactions(blocks):
    trx = []
    for block in blocks:
        for transaction in block.transactions:
            trx.append(dict(transaction))
    for transaction in trx:
        if "accessList" in transaction:
            del transaction["accessList"]
        transaction['blockHash'] = transaction['blockHash'].hex()
        transaction['hash'] = transaction['hash'].hex()
        transaction['input'] = transaction['input'].hex()
        transaction['r'] = transaction['r'].hex()
        transaction['s'] = transaction['s'].hex()
    return trx

def extract_blocks(blocks):
    exclude_fields = ['transactions', 'withdrawals', 'uncles']
    dict_blocks = []
    for block in blocks:
        dict_block = dict(block)
        for key, value in block.__dict__.items():
            if (key in exclude_fields):
                dict_block.pop(key, None)
                continue
            if isinstance(value, bytes):
                dict_block[key] = value.hex()
        dict_blocks.append(dict_block)
    return dict_blocks

def extract_withdrawals(blocks):
    withdrawals = []
    for block in blocks:
        for withdrawal in block.withdrawals:
            wd = dict(withdrawal)
            wd['blockNumber'] = block.number
            withdrawals.append(wd)
    return withdrawals
