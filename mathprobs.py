from random import shuffle

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

def spy_game_long(list):
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

def spy_game_short(list):
    temp_list=[0,0,7,'x']
    for num in list:
        if num==temp_list[0]:
            temp_list.pop(0)
    if len(temp_list)==1:
        print('I am James Bond 007.Friends call me Siva')
    else:
        print('This is not 007 list')

'''Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
def unique_list(list):
       print([item for item in set(list)])

def fibonoccigenerator():
    '''Generator that generates the fibonocci series upto number n'''
    number=int(input('Enter the number to generate fibonocci upto : '))
    def fibgen():
        a=1
        b=1
        for item in range(number):
            while(a<=number):
                yield a
                a,b=b,a+b
    for item in fibgen():
        print(item)

def randonnumgenerators():
    '''Geneartor for n randon numbers in range low and high'''
    low=int(input('Enter lower limit to generate random numbers : '))
    high= int(input('Enter higher limit to generate random numbers : '))
    n= int(input('Enter how many random numbers you want : '))
    mylist=[num for num in range(low,high)]
    shuffle(mylist)
    def randomgen():
        counter=0
        for number in mylist:
            if counter<n:
                yield number
                counter+=1
    for number in randomgen():
                print(number)