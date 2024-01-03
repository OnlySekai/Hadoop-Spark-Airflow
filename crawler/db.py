import json


def load_db():
    with open('db.json') as f:
        db = json.load(f)
    last_block = db.get('last_block', 0)
    block_step = db.get('block_step', 20)
    return last_block, block_step


def save_db(last_block, block_step=20):
    db = {
        'last_block': last_block,
        'block_step': block_step
    }
    with open('db.json', 'w') as f:
        json.dump(db, f)
