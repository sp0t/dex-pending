import time
from threading import Thread
from web3 import Web3
import abis
import os
from dotenv import load_dotenv

load_dotenv()

contractAddress = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
chainId = 56
abi = abis.pancake_abi
public_key = os.getenv('PUBLICK_KEY')
private_key = os.getenv('PRIVATE_KEY')
w3 = Web3(Web3.HTTPProvider("https://bsc-mainnet.nodereal.io/v1/58e77623029c44f19e710581ef96915d", request_kwargs={'timeout': 60}))
# Connect to Binance Smart Chain node
web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org'))
swap_router = web3.eth.contract(address=contractAddress, abi=abi)

def validateTx(transaction):
    return 0

    if transaction['input'][:10] != '0x7ff36ab5':
        return -1
    
    path_str = transaction['input'][-128:]
    path1 = '0x' + path_str[24:64]
    path2 = '0x' + path_str[88:128]
    
    if path1 == '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c' and path2 == '0xfe9803c5775a7311da5a60bbc3a60946dc335a28':
        return 0
    else:
        return -2
  
def makeSwap(transaction):

    # pending_tx_count = w3.eth.get_block('pending').transactions
    print("pending_tx_count")
    
    # print(f"Gas price: {gas_price}, Pending txs: {num_pending_txs}")
    # Check if the gas price is below the threshold and the number of pending transactions is low
    # if gas_price < gas_price_threshold and num_pending_txs < 100:
    #     # Submit your transaction here
    #     print("Submitting transaction...")
        
    # if validateTx(transaction) == 0:
    #     print('OK', transaction)
    #     ts1 = time.time()
    #     add_tx = swap_router.functions.swapExactETHForTokens(1, [w3.toChecksumAddress('0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'),w3.toChecksumAddress('0xfE9803C5775a7311dA5a60BbC3a60946Dc335A28')], public_key, 9999999999999)
    #     nonce = w3.eth.get_transaction_count(public_key)
    #     gas = transaction['gas']
    #     gasprice = transaction['gasPrice']
    #     print(gas, gasprice)
    #     add_tx = add_tx.buildTransaction({'from': public_key, 'chainId': chainId, 'nonce': nonce ,'value': 100000000, 'gasPrice': 6000000000, 'gas': 160842})
    #     tx_create = w3.eth.account.sign_transaction(add_tx, private_key)
    #     txn_hash = w3.eth.sendRawTransaction(tx_create.rawTransaction)
    #     w3.eth.wait_for_transaction_receipt(txn_hash)
    #     ts2 = time.time()
    #     print('time======>', ts2-ts1)
          
# Create and launch a thread
def startSwap(transaction):    
    t = Thread(target = makeSwap, args =(transaction, ))
    t.start() 