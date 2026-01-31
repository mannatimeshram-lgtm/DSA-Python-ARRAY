"""1.print all elements of : 
arr=[5,10,15,20]
2. insert 25 at index 2 and print array
3. delete element at index 1
4. find max element manually
"""
from array import *
arr= array( 'i', [ 5 , 10 , 15 , 20 ])

for i in arr:
    print( i , end=" ")

print("\n")

arr.insert(2,25)
for i in arr:
    print( i , end=" ")

print("\n")

arr.pop(1)
for i in arr:
    print( i , end=" ")

print("\n")

maxEl= arr[0]
for m in range(1,len(arr)):
    if arr[m]> maxEl:
        maxEl= arr[m]

print(" maximum element :" , maxEl)
