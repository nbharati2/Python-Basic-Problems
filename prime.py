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
    
