


def total(num):
    total = 0 
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0: 
            total += i
    
    return total
            