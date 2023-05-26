import matplotlib.pyplot as mpl
import numpy as np

lst=np.random.randint(0,100,25)
x=np.arange(0,25,1)
n=len(lst)

# BUBBLE SORT

for i in range(n):
    for j in range(0,n-1-i):
        mpl.bar(x,lst)
        mpl.pause(0.1)
        mpl.clf()
        if(lst[j]>lst[j+1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]

mpl.show()
