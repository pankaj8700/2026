l1 = [10, 5,2,9,6]
def quick(l1):
    if len(l1)<= 1:
        return l1
    pivot = l1[0]
    high = [x for x in l1[1:] if x >= pivot]
    low = [x for x in l1[1:] if x < pivot]
    return quick(low) + [pivot] + quick(high)
    
def bubble_sort(l1, search):
    index = -1
    sorted_arry = quick(l1)
    print(sorted_arry)
    low = mid = 0
    high = len(sorted_arry) - 1
    while low <= high:
        mid = (low + high)//2
        if sorted_arry[mid] == search:
            print(f"value at {mid} index")
            break
        elif sorted_arry[mid] > search:
            high = mid-1
            print("high:",high)
        else:
            low = mid + 1
            print("low:", low)

print(bubble_sort(l1,10))