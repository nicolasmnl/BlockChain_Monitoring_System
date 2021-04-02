from block.block import Block


class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def add_block(self, block):
        self.chain.append(block)

    def create_genesis_block(self):
        block = Block(0, "27/03/2021", "0", "Genesis Block")
        self.chain.append(block)

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def exibe_blocos(self):
        s = ""
        for b in self.chain:
            s += str(b) + "\n"

        return s
