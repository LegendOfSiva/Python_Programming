def string_reversal():
        input_string=input('Enter the input String \n ')
        print(input_string[::-1])  

def count_string_chars():
        mydict={}
        input_string=input('Enter the input String \n ')
        for item in input_string:
                if item not in mydict:
                        mydict[item]=1
                else :
                        mydict[item]=mydict.get(item)+1
        print(mydict)

def sentence_reversed():
    sentence=input("Enter any sentence \n ")
    mylist=sentence.split()
    index=-1
    output=''
    for item in mylist:
        output=output+ mylist[index]+" "
        index=index-1
    print(output)