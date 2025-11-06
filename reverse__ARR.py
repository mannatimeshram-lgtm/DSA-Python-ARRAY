#que= reverse an given array without using slicing or reverce() function .

arr= [10,20,30,40,50]

start=0
end = len(arr)-1

while start<end :
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1

print ( "reverse array:" , arr)

