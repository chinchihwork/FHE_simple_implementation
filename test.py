import numpy as np

i = 1309419188 * 2167103797 + 3558497559
q = i % 3034700497
t = q / 11808 
print(i  ,q , t)

# 3196581315

import numpy as np

array1 = np.array([1309419188])
array2 = np.array([2167103797])
array3 = np.array([3558497559])

print(type(array1[0]))
result = array1 * array2 + array3
print(result , result % 3034700497)