
import numpy as np

class KEY_GEN():
    def __init__(self , s:str):
        if not isinstance(s , str):
            raise TypeError("Please type in a string")
        if (len(s) > 8):
            raise TypeError("At most 8 character available")
        pass
    