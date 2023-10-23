
import numpy as np
import random

class  ENCRYPT_N_DECRYPT:
    module = 3034700497
    small_module = 257003
    delta = int(module / small_module)

    def __init__(self , secret_key : int):
        self.key = secret_key

    # max integer we can encrypt is less than 257003
    def encrypt(self , message : int) -> np.array:
        if (message >= ENCRYPT_N_DECRYPT.small_module):
            raise OverflowError("Overflow , max integer = 257003")
        encrypted_message_2 = np.int64(random.randint(0 , ENCRYPT_N_DECRYPT.module))
        encrypted_message_1 = np.int64((message * ENCRYPT_N_DECRYPT.delta + (self.key * encrypted_message_2) * (-1)) % ENCRYPT_N_DECRYPT.module)
        encrypted_message = np.array([encrypted_message_1 , encrypted_message_2])
        return encrypted_message
    
    def decrypt(self , encrypted_message : np.array):
        m0 = encrypted_message[0]
        m1 = encrypted_message[1]
        decrypted_message = (((m1) * self.key % ENCRYPT_N_DECRYPT.module + m0) % ENCRYPT_N_DECRYPT.module)
        decrypted_message = int(decrypted_message / ENCRYPT_N_DECRYPT.delta)
        return (decrypted_message)
    
if __name__ == "__main__":
    key = random.randint(0 , ENCRYPT_N_DECRYPT.module)
    print(f"Key : {key}")
    encrypter = ENCRYPT_N_DECRYPT(key)
    message = random.randint(0 , ENCRYPT_N_DECRYPT.small_module)
    print(f"Message :{message}")
    encrypted_message = encrypter.encrypt(message)
    print(f"Encrypted message : {encrypted_message}")
    decrypted_message = encrypter.decrypt(encrypted_message)
    print(f"decrypted message : {decrypted_message}")
    pass