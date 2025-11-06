arr= [10,20,30,40,50]

largest= arr[0]
smallest=arr[0]

for num in arr:
    if num > largest:
        largest=num 
    if num < smallest:
        smallest = num 

print("largest:", largest)
print("smallest:", smallest)