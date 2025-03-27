import time 
n=1000
l1=[[i for i in range(n)] for i in range(n)]
l2=[[i for i in range(n)] for i in range(n)]
# start=time.time()
# for i in range(n):
#     for j in range(n):
#         l1[i][j]+l2[i][j]
# end=time.time()
# print(end-start)


import numpy as np
start=time.time()
m1=np.array(l1)
m2=np.array(l2)

m1+m2
end=time.time()
print(end-start)
