import win32clipboard

from typing import Union

class clipboard: 
    def __init__(self) -> None:
        pass
    
    def contents() -> Union[str, None]:
        """Get clipboard contents and return it if anything is there.

        Returns:
            Union[str, None]: Return clipboard content or None if nothing is copied.
        """
        try:
            win32clipboard.OpenClipboard()
            content = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            
            if content == "" or content == " " or content == None: 
                return None
            else: 
                return content
        except:
            return None
        
    def set_contents(content: str) -> bool:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(content)
            win32clipboard.CloseClipboard()
            return True
        except:
            return False