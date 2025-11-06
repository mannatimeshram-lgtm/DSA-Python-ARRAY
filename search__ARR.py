# que = using linear search find the element in array by taking input .

arr= [10,20,30,40,50]

num=int(input('enter a number :'))

found= False 
for i in range(len(arr)):
    if arr[i]==num:
        print(f"FOUND at index{i}")
        found=True
        break
if not found:
    print('NOT in arr')
    



