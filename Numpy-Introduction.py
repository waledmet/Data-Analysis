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

#Numpy Operations
a = np.arange(4)
print("a=",a)
print("a+10 = ",a+10)
print("a*10 = ",a*10)
a += 100
print("a=",a)
l=[0,1,2,3]
print("(i*10 for i in l) = ",(i*10 for i in l))
a=np.arange(4)
b=np.array([10,10,10,10])
print("a+b = ",a+b)

#Numpy Boolean Arrays

a = np.arange(4)
print("a = ",a)
print("a[[0,-1]] = ",a[[0,-1]])
print("a[[True,False,False,True]] = ",a[[True,False,False,True]])
print("a >=2 = ",a >=2)
print("a[a >=2] = ",a[a >=2])
print("a.mean() = ",a.mean())
print("a[a > a.mean()] = ",a[a > a.mean()])
print("a[~(a > a.mean())] = ",a[~(a > a.mean())])
print("a[(a==0) | (a ==1)] = ",a[(a==0) | (a ==1)])
print("a[(a <= 2) & (a % 2 ==0)] = ",a[(a <= 2) & (a % 2 ==0)])
A=np.random.randint(100,size=(3,3))
print("A = ",A)

#Numpy Algebra and Size
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
B = np.array([
    [6,5],
    [4,3],
    [2,1]
])
print("A.dot(B) = ",A.dot(B))
print("A @ B = ",A @ B)
print("B.T = ",B.T)
print("B.T @ A = ",B.T @ A)

print("sys.getsizeof(1)= ",sys.getsizeof(1)," bytes") 
print("sys.getsizeof(10**100)= ",sys.getsizeof(10**100)," bytes") 
print("np.dtype(int).itemsize= ",np.dtype(int).itemsize)
print("np.dtype(float).itemsize= ",np.dtype(float).itemsize)
print("np.dtype(np.int8).itemsize= ",np.dtype(np.int8).itemsize)
print("sys.getsizeof([1]) = ",sys.getsizeof([1])," bytes")
print("np.array([1]).nbytes = ",np.array([1]).nbytes)

l =list(range(1000))
a = np.arange(1000)
print("sum([x **2 for x in l]) = ",sum([x **2 for x in l]))
print("np.sum(a **2) = ",np.sum(a **2))


#random
print("np.random.random(size=2) = ",np.random.random(size=2))
print("np.random.normal(size=2) = ",np.random.normal(size=2))
print("np.random.rand(2,4) = ",np.random.rand(2,4))

#arange
print("np.arange(10) = ",np.arange(10))
print("np.arange(5,10) = ",np.arange(5,10))
print("np.arange(0,1,.1) = ",np.arange(0,1,.1))

# reshape
print("np.arange(10).reshape(2,5) = ",np.arange(10).reshape(2,5))
print("np.arange(10).reshape(5,2) = ",np.arange(10).reshape(5,2))

#linspace
print("np.linspace(0,1,5) = ",np.linspace(0,1,5))
print("np.linspace(0,1,20) = ",np.linspace(0,1,20))
print("np.linspace(0,1,20,False) = ",np.linspace(0,1,20,False))

#zeros , ones ,empty
print("np.zeros(5) = ",np.zeros(5))
print("np.zeros((3,3)) = ",np.zeros((3,3)))
print("np.zeros((3,3, dtype=np.int8 = ",np.zeros((3,3), dtype=np.int8))
print("np.ones(5) = ",np.ones(5))
print("np.empty(5) = ",np.empty(5))
print("np.empty((2,2)) = ",np.empty((2,2)))

#identity , eye
print("np.identity(3) = ",np.identity(3))
print("np.eye(3,3) = ",np.eye(3,3))
print("np.eye(8,4) = ",np.eye(8,4))
print("np.eye(8,4,k=1) = ",np.eye(8,4,k=1))