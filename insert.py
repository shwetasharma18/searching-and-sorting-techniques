def insertion_sort(num):
    i = 1
    
    while i < len(num):
    
        temp = num[i]
    
        j = i - 1
    
        while j >= 0 and temp < num[j]:
    
            num[j+1] = num[j]
            
            j = j -1
        
        num[j+1] = temp
        
        i = i + 1
        
    return num

l = [5,7,3,9,8,2,4,1]

print insertion_sort(l)