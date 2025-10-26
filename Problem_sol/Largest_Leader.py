arr = [11,2,3,4,12,54,34,9]

leader = []

mx_ele = arr[-1]
leader.append(mx_ele)

for i in range(len(arr)-2,-1,-1):
    if arr[i]>mx_ele:
        mx_ele = arr[i]
        leader.append(mx_ele)   
print(leader)