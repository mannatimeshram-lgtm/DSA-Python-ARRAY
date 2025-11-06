arr= [ 1,2,3,4,1,2,3,4,5,6,2,3,5,7,8,7,4,3]

freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
    

for key,value in freq.items():
    print(key,"-",value,"time's")
