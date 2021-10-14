# QUESTION - 1
import numpy as np
arr=np.ones(10)*5
print("Array of 10 fives:")
print(arr)
print()

# QUESTION - 2
import numpy as np
arr=np.arange(10,51)
print(arr)
print()

# QUESTION - 3
import numpy as np
arr=np.arange(10,51,2)
print(arr)
print()

# QUESTION - 4
import numpy as np
x = np.arange(0,9).reshape(3,3)
print(x)
print()

# QUESTION - 5
import numpy as np
rand_num = np.random.normal(0,1,25)
print("Random Numbers => ")
print(rand_num)
print()

# QUESTION - 6
import numpy as np
arr=np.arange(0,1.01,0.01)
print(arr)
print()

# QUESTION - 7
import numpy as np
arr=np.linspace(0,1,20)
array = ['{:.2f}'.format(x) for x in arr]
print(array)
print()

# QUESTION - 8
import numpy as np
mat=np.arange(1,26).reshape(5,5)
print(mat)
arr1 = mat[2:,:]
print(arr1)
arr2 = mat[0:3,1:2]
print(arr2)
print(np.sum(mat))
print(np.sum(mat,axis=1))
print(np.sum(mat,axis=0))