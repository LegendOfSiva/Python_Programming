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
    output=mylist[::-1]
    print(' '.join(output))

def paper_doll():
        input_string=input('Enter any String \n ')
        output=''
        for item in input_string:
              output=output+(item*3)
        print(output)