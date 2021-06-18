import math

count = 0

def is_prime(i):
    for check in range(2, (int(math.sqrt(i))+1)):
        if i % check == 0:
            break
            return 0

    else:
        if i != 1:
            return 1

num = int(input("Enter the number: "))

for j in range(2, num//2 + 1):
    if is_prime(j) == True:
        if is_prime(num-j) == True:
            print(num,"=", j,"+",num-j)
            count = count+1

print("No.of ways",num, "can be expressed as the sum of two primes:", count)
