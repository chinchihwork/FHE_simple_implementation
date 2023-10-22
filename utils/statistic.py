
import numpy as np
import pandas as pd
import csv


class MODULE_RING_OPE() :
    module = 4294475777
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
        return (len(ret) , ret)

    def sum_of_the_score (self , scores : np.array) -> np.int64 :
        sum = np.int64(0)
        for i in scores:
            sum += i
        return sum
        
if __name__ == "__main__":
    test = MODULE_RING_OPE("StudentsPerformance.csv")
    print(test.data)