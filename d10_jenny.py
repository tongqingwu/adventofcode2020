from datetime import datetime

def find_p(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return find_p(n - 1) + find_p(n - 2) + find_p(n - 3)

def find_p_no_recursive(n):
    list1 = [1,1,2,4]
    while (n != len(list1)):
        list1.append(list1[-1]+list1[-2]+list1[-3])
    print(list1)
    
    return list1[-1]
 
print(datetime.now())
#print(find_p(5))
print(find_p_no_recursive(5))
print(datetime.now())

