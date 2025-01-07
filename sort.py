import random
cnt =0
def merge(list1,list2):
    result = []
    i = j = 0
    m = len(list1)
    n = len(list2)


    while i < m and j < n :
        if list1[i] < list2[j]:
            result.append(list1[i])
            i = i + 1

        else:
            result.append(list2[j])
            j = j + 1
    
    if i < m:
        result.extend(list1[i:])

    elif j < n:
        result.extend(list2[j:])

    return result

def mergesort(lst): #Dividing the list into two equal halves
     length = len(lst)
     global cnt
     
     #Base condition
     if length < 2:
        return lst[:]
        

     #Performing recurion till list is broken down into single element
     else:
        mid = length // 2
        
        cnt +=1
        
        return merge(mergesort(lst[:mid]),mergesort(lst[ mid :]))
     
def BinarySearch(lst,srch):
    low = 0
    high = len(lst)-1
    mid = (low+high)//2

    if len(lst) == 1:
        if srch in lst:
            return "Element  Found"
        
        else:
            return "Element not found"
    
    else:

        if srch < lst[mid]:
            return BinarySearch(lst[low:mid-1],srch)
        
        elif srch > lst[mid]:
            return BinarySearch(lst[mid+1:high],srch)
        
        elif srch == lst[mid]:
            return "Element Found"
        

#Main
if __name__ == "__main__":


    #Defining empty ist
    lst = []

    #Reading value of n from user
    num = int(input("Enter number of values-->"))
        

    #Appending random values to the list
    for i in range(num):
            elem = random.randint(1,100)
            lst.append(elem)

    #Unsorted list
    print("The list-->",lst)

    #Sorted list
    sorted_list = mergesort(lst)
    print(sorted_list)

    srch = int(input("Enter the element you want to search from the list??"))
    print(BinarySearch(sorted_list,srch))
    
def Quicksort():
    


          
