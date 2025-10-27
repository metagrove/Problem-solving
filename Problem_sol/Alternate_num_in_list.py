"""
Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12
"""
def alternates(array):
    alter = []
    for i in range(0,len(array),2): #TRAVERSING THE ARRAY WITH A STEP OF 2
        alter.append(array[i])
    return alter

arr= [10, 20, 30, 40, 50]
print(alternates(arr))

arr = [10, 20, 30, 40, 50]  # ARRAY OF ELEMENTS

