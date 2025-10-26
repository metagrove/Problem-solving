arr = [11,2,3,4,12,54,34,9]       #ARRAY OF ELEMENTS

leader = []                       #LIST TO STORE LEADER ELEMENTS

mx_ele = arr[-1]                  #INITIALIZING MAXIMUM ELEMENT WITH LAST ELEMENT
leader.append(mx_ele)             #ADDING LAST ELEMENT TO LEADER LIST

for i in range(len(arr)-2,-1,-1): #TRAVERSING THE ARRAY FROM SECOND LAST ELEMENT TO FIRST
    if arr[i]>mx_ele:             #IF CURRENT ELEMENT IS GREATER THAN MAXIMUM ELEMENT
        mx_ele = arr[i]           #UPDATING MAXIMUM ELEMENT
        leader.append(mx_ele)     #ADDING CURRENT ELEMENT TO LEADER LIS
print(leader)                     #PRINTING THE LEADER ELEMENTS