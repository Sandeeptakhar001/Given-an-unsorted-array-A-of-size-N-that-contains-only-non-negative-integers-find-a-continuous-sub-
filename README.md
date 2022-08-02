# Given-an-unsorted-array-A-of-size-N-that-contains-only-non-negative-integers-find-a-continuous-sub-

n = int(input())

dig = 0

while n >0:
    
    rev = n%10
    
    dig += rev
    
    n = n//10
    
print(dig)

