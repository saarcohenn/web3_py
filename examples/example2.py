from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account1 = "0x0Cb60ED96576AdE69f5a135a256AD53D6815e6B6"
account2 = "0xa72A0A4a828e9893D9e571250099158F96c1072A"

private_key = "29da97b4add3d7c6a69a353499c69427eea8eab5fb6a25f895114307ca33be26"

# get the nodes
nonce = web3.eth.getTransactionCount(account1)

# build a transaction
tx = {
    'nonce': nonce,
    'to': account2,
    'value': web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50','gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction and get hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))