import numpy as np
print(np.__version__)
print("hello")

a = np.array([1,2,3,4,5,6])
b=np.where(a%2==0)
print(b)

d = np.array([[1,2,3,4],[5,5,6,6]])
print(np.sort(d))

print(np.random.randint(1009))
c=np.zeros(2)
print(c)
