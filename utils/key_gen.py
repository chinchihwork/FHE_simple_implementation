
import numpy as np

class KEY_GEN():
    t = 257003
    q = 4294967291
    acceptable_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_62_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
    def __init__(self , s:str):
        if not isinstance(s , str):
            raise TypeError("Please type in a string")
        if (len(s) > 8):
            raise TypeError("At most 8 character available")
        self.s = s 
        self.char_to_prime = KEY_GEN.create_dictionary_from_two_list(KEY_GEN.acceptable_characters , KEY_GEN.first_62_prime)
        self.key_value = self.password_to_key_value()
        pass
    
    @staticmethod
    def create_dictionary_from_two_list(keys , values):
        if (len(keys) != len(values)):
            print(len(keys))
            print(len(values))
            raise TypeError("check the length of the lists first")
        my_dict = {}

        for index, key in enumerate(keys):
            my_dict[key] = values[index]
        return my_dict

    def password_to_key_value(self):
        key_value = 1
        for index , c in enumerate(self.s):
            i = self.char_to_prime[c]
            key_value *= i ** c % KEY_GEN.q
        

if __name__ == '__main__':
    print(len(KEY_GEN.acceptable_characters))
    print(len(KEY_GEN.first_62_prime))
    gene = KEY_GEN("cat77")
    
    pass
        