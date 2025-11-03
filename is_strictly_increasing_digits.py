def is_strictly_increasing_digits(n):

    if type (n) != int:
        return -1 
    if n < 0 :
        return -1 
    
    n = str(n)
    if len(n) == 1:
        return True
    i = 0
    
    while True:
        if i + 1 == len(n):
            break
        if n[i] >= n[i + 1]:
            return False
    
        i = i+1
    return True


print(is_strictly_increasing_digits(1234))
print(is_strictly_increasing_digits(-1234))
print(is_strictly_increasing_digits(321))
print(is_strictly_increasing_digits(8.91234))




#1) is_strictly_increasing_digits(n)
   #- Return True if the digits of a non-negative integer n are strictly increasing from left to right
  # - Return False otherwise
   #- Return -1 if n is negative or not an intiger
   
