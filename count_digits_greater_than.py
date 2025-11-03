def count_digits_greater_than(n, t):
    if type (n) != int or type (t) != int:
        return -1
    if n<0:
        return -1
    if t<0 or t>9 :
        return -1
    n = str(n)
    count = 0
    for i in n:
        if int(i)>t:
            count = count + 1
    return count

print(count_digits_greater_than(351292, 3))
print(count_digits_greater_than(888, 8))
print(count_digits_greater_than(-45, 3))