
import numpy as np
import pandas as pd
import csv


class MODULE_RING_OPE() :
    module = 3034700497
    def __init__ (self , data_path : str):        
        self.data = MODULE_RING_OPE.csv_to_numpy_array(data_path)

    @staticmethod
    def csv_to_numpy_array(file_path):
        data_frame = pd.read_csv(file_path)
        np_array = data_frame.to_numpy()
        # test test
        list = []
        for i in np_array:
            list.append(i[-1])
        ret = np.array(list)        
        # test test
        return ret

    def cypher_text_sum (self , numbers : np.array) -> np.int64 :
        
        sum0 = 0
        sum1 = 0
        for i in numbers:
            sum0 = (sum0 + i[0]) % MODULE_RING_OPE.module
            sum1 = (sum1 + i[1]) % MODULE_RING_OPE.module
        return np.array([sum0 , sum1])
        
if __name__ == "__main__":
    test = MODULE_RING_OPE("StudentsPerformance.csv")
    # print(test.data)
    test_array = np.random.randint(low = 1 , high = 100 , size = 100)
    test_array2 = np.array([1,2])
    print(test_array)
    print(sum(test_array))

    from encrypt_decrypt import ENCRYPT_N_DECRYPT
    import random
    
    key = random.randint(2000000000 , MODULE_RING_OPE.module)
    e_n_d = ENCRYPT_N_DECRYPT(key)
    print(f"Key : {e_n_d.key}")
    encrypted_data = []
    for number in test_array:
        encrypted_data.append(e_n_d.encrypt(number))
    # print(f"Encrypted data : {encrypted_data}")
    
    encrypted_sum = test.cypher_text_sum(encrypted_data)
    print(f"Encrypted sum : {encrypted_sum}")
    print(f"Key : {e_n_d.key}")

    sum = e_n_d.decrypt(encrypted_sum)
    print(f"Decrypted sum : {sum}")


