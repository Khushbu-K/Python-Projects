# Check if the number is a prime number:

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print(False) 
    print(True) 
        
is_prime(73) 