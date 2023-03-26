import re

from hashlib import sha256

class bitcoin: 
    def __init__(self) -> None:
        pass 
    
    def is_valid_address(address: str) -> bool: 
        address_detection_regex = "^(1|[13][a-km-zA-HJ-NP-Z0-9]{25,34}|(bc1|[02-9ac-hj-np-z]{1})[a-zA-HJ-NP-Z0-9]{16,100})$"
        
        return bool(re.match(address_detection_regex, address))