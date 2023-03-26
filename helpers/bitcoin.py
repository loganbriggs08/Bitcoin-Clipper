import re

class bitcoin: 
    def __init__(self) -> None:
        pass 
    
    def is_valid_address(string: str) -> bool: 
        """Check if a string is a valid bitcoin address.

        Args:
            string (str): String to check for an address.
        Returns:
            bool: Return if the string contains a valid address.
        """
        address_detection_regex = "^(1|[13][a-km-zA-HJ-NP-Z0-9]{25,34}|(bc1|[02-9ac-hj-np-z]{1})[a-zA-HJ-NP-Z0-9]{16,100})$"
        
        return bool(re.match(address_detection_regex, string))