
import numpy as np
import random

class  ENCRYPT_N_DECRYPT():
    module = np.int64(4294475777)
    small_module = np.int64(257003)
    delta = int(module / small_module)

    def __init__(self , secret_key : int):
        self.key = secret_key

    # max integer we can encrypt is less than 257003
    def encrypt(self , message : int) -> np.array:
        if not isinstance(message , int):
            raise TypeError("Need an integer")
        if (message >= 257003):
            raise OverflowError("Overflow , max integer = 257003")
        encrypted_message_2 = np.int64(random.randint(0 , ENCRYPT_N_DECRYPT.module))
        encrypted_message_1 = np.int64((message * ENCRYPT_N_DECRYPT.delta + (self.key * encrypted_message_2) * (-1)) % ENCRYPT_N_DECRYPT.module)
        encrypted_message = np.array([encrypted_message_1 , encrypted_message_2])
        return encrypted_message
    
    def decrypt(self , encrypted_message : np.array) -> int:
        decrypted_message = ((encrypted_message[1] * self.key + encrypted_message[0]) % ENCRYPT_N_DECRYPT.module) / ENCRYPT_N_DECRYPT.delta
        return (np.int64(decrypted_message) , type(decrypted_message))
    
if __name__ == "__main__":
    key = random.randint(0 , ENCRYPT_N_DECRYPT.module)
    print(key)
    encrypter = ENCRYPT_N_DECRYPT(key)
    message = random.randint(0 , ENCRYPT_N_DECRYPT.small_module)
    print(message)
    encrypted_message = encrypter.encrypt(message)
    print(encrypted_message)
    decrypted_message = encrypter.decrypt(encrypted_message)
    print(decrypted_message)
    pass