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
