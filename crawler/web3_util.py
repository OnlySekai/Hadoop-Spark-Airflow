from web3 import Web3

from constants import RPC


class Web3Util:
    def __init__(self, provider):
        self.web3_instance = Web3(provider)

    def get_block(self, block_number):
        try:
            block = self.web3_instance.eth.get_block(block_number, True)
            return block
        except Exception as e:
            raise Exception("Could not get information of getBlock") from e


web3Util = Web3Util(Web3.HTTPProvider(RPC))
