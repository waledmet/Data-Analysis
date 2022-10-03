#pip install numpy
import numpy as np 
import sys
n=3

arr1=np.array([1,2,3,4])
print("arr1=",arr1)
print("arr1.sum()=",arr1.sum())
print("arr1[0:]=",arr1[0:])
print("arr1[1:3]=",arr1[1:3])
print("arr1[1:-1]=",arr1[1:-1])
print("arr1[::2]=",arr1[::2])
print("arr1[-1]=",arr1[-1])
print("arr1[[0,2,-1]]=",arr1[[0,2,-1]])
print("arr1.dtype=",arr1.dtype)

#small integer for performance
arr2 = np.array([1,2,3,4],dtype=np.int8)
print("arr2=",arr2)

#set in float 
arr3 = np.array([1,2,3,4],dtype=np.float64)
print("arr3=",arr3)

#multi object
arr4 = np.array([{"A":1},sys])
print("arr4.dtype=",arr4.dtype)

# two dimensions
arr5 = np.array([
    [1,2,3],
    [4,5,6]
])
print("arr5.shape=",arr5.shape)
print("arr5.ndim=",arr5.ndim)
print("arr5.size=",arr5.size)

# three dimensions
arr6 = np.array([
    [
        [12,11,10],
        [9,8,7]
    ],
    [
        [6,5,4],
        [3,2,1]
    ]

])

print("arr6.shape=",arr6.shape)
print("arr6.ndim=",arr6.ndim)
print("arr6.size=",arr6.size)

#index 
arr7=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("arr7[1]=",arr7[1])
print("arr7[1][0]=",arr7[1][0])
print("arr7[0:2]=",arr7[0:2])
print("arr7[::2]=",arr7[::2])
print("arr7[:,:2]=",arr7[:,:2])
print("arr7[:2,:2]=",arr7[:2,:2])
print("arr7[:2,2:]=",arr7[:2,2:])


#summary statistics
arr8=np.array([1,2,3,4])
print("arr8.sum()=",arr8.sum())
print("arr8.mean()=",arr8.mean())
print("arr8.std()=",arr8.std())

arr9 = np.array([
    [1,2,3],
    [4,5,6]
])

print("arr9.sum()=",arr9.sum())
print("arr9.mean()=",arr9.mean())
print("arr9.sum(axis=0)=",arr9.sum(axis=0))
print("arr9.sum(axis=1)=",arr9.sum(axis=1))
print("arr9.mean(axis=0)=",arr9.mean(axis=0))
print("arr9.mean(axis=1)=",arr9.mean(axis=1))