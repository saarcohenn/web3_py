from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/1e1a1ab6cca7416bb97063fea21d5d8c"
web3 = Web3(Web3.HTTPProvider(infura_url))

latestBlock = web3.eth.blockNumber
print(latestBlock)
print(web3.eth.getBlock(latestBlock))