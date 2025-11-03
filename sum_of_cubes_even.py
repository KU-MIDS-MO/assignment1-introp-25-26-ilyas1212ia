def sum_of_cubes_even(n):

    if type (n) != int:
        return -1
    if n<0 :
        return -1
    if n>2000:
        print ("warning!! n is too large, its greater trhan 2000")
        
    total = 0
    for i in range (0, n+1):
          if i % 2 == 0:
            total = total + (i**3)
    return float(total)
            
            
print(sum_of_cubes_even(10))
 