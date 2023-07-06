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

def has33(list):
    index=0
    checker=False
    for item in list:
        if list[index]==3 and index < (len(list)-1): 
            if list[index+1]==3:
                print('True, it contains 3,3 successively')
                checker=True
                break
            else:
                pass
        else :
             pass
        index+=1
    if(not checker):
        print("False, it doesn't contains 3,3 successively")

def spy_game(list):
    final_list=[]
    checker=False
    index=0
    for item in list:
        if item==0 or item==7:
            final_list.append(item)
        else :
            pass
    for item2 in final_list:
        if final_list[index]==0 and index < (len(final_list)-2):
            if final_list[index+1]==0:
                if final_list[index+2]==7:
                    print('I am James Bond 007.Friends call me Siva')
                    checker=True
                    break
                else :
                    pass
            else :
                pass
        else :
            pass
        index+=1
    if (not checker):
        print('This is not 007 list')
