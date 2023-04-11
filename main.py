
from web3.auto import Web3
import swapthread
import asyncio
import json
import time

# w3 = Web3(Web3.HTTPProvider("https://bsc-mainnet.nodereal.io/v1/58e77623029c44f19e710581ef96915d", request_kwargs={'timeout': 60}))
# w3 = Web3(Web3.HTTPProvider("https://bsc-mainnet.nodereal.io/v1/1f70e06dce7c42ac916e2236a34b89fc", request_kwargs={'timeout': 60}))
w3 = Web3(Web3.WebsocketProvider("wss://bsc-mainnet.nodereal.io/ws/v1/58e77623029c44f19e710581ef96915d", websocket_timeout=10))
print(w3.is_connected())
router = w3.to_checksum_address('0x10ED43C718714eb63d5aA57B78B54704E256024E')


def handle_event(event):
    try:
        transaction = w3.to_json(event).strip('"')
        print(transaction)
        print(time.time())
        transaction = w3.eth.get_transaction(transaction)
        to = transaction['to']

        # if to == router:
        # swapthread.startSwap(transaction)
    except Exception as err:
        print(f'error: {err}')


async def log_loop(event_filter):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)

def main():
    tx_filter = w3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(tx_filter)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()