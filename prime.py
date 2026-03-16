num = int(input("Enter a number: "))

if num < 2:
    print("Not prime")
else:
    for i in range(2, num):
        print(i)
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
    
#Write a Python function called `is_prime(n)` that takes an integer `n` and returns `True` if the number is prime, and `False` otherwise.
def is_prime(n):
    if n < 2:
        return False
        
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
    
print(is_prime(37))
            
