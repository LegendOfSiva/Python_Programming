def prime_checker():
    num = int(input("Enter a number: \n "))
    prime_flag = False
    if num > 1: 
        for i in range(2, int(num**0.5)+1):
            if (num % i) == 0:
                # if factor is found, set flag to True
                prime_flag = True
                # break out of loop
                break
        # check if flag is True or False
        if prime_flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
