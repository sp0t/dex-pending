
from web3.auto import Web3
import swapthread
import asyncio
import json
import time

web3 = Web3(Web3.HTTPProvider("https://bsc-mainnet.nodereal.io/v1/58e77623029c44f19e710581ef96915d", request_kwargs={'timeout': 60}))


# Check to see if you are connected to your node
print(web3.isConnected())

# add an address you want to filter pending transactions for
# make sure the address is in the correct format
router = web3.toChecksumAddress('0x10ED43C718714eb63d5aA57B78B54704E256024E')


def handle_event(event):

    try:
        # remove the quotes in the transaction hash
        transaction = Web3.toJSON(event).strip('"')
        # use the transaction hash (that we removed the '"' from to get the details of the transaction
        transaction = web3.eth.get_transaction(transaction)
        # set the variable to the "to" address in the message
        to = transaction['to']

        # if to in dex_list['dex']:
        #     #check if transaction is swap
        #     if transaction['input'][:10] in dex_list[to]:
        #         swapthread.startSwap(transaction)
        if to == router:
            # print('=========', transaction['blockNumber'], '===========')
            # print(transaction)
            print('time=================> 2', time.time())
            swapthread.startSwap(transaction)
        # else:
        #     print('Not what we are looking for')
    except Exception as err:
        # print transactions with errors. Expect to see transactions people submitted with errors
        print(f'error: {err}')


async def log_loop(event_filter):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)

def main():
    # filter for pending transactions
    tx_filter = web3.eth.filter('pending')
    print('time=================> 3', time.time())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(tx_filter)))
    finally:
        loop.close()


if __name__ == '__main__':
    main()