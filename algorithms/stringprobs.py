import string


def string_reversal():
    input_string = input("Enter the input String \n ")
    print(input_string[::-1])


def count_string_chars():
    mydict = {}
    input_string = input("Enter the input String \n ")
    for item in input_string:
        if item not in mydict:
            mydict[item] = 1
        else:
            mydict[item] = mydict.get(item) + 1
    print(mydict)


def sentence_reversed():
    sentence = input("Enter any sentence \n ")
    mylist = sentence.split()
    output = mylist[::-1]
    print(" ".join(output))


def paper_doll():
    input_string = input("Enter any String \n ")
    output = ""
    for item in input_string:
        output = output + (item * 3)
    print(output)


"""Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

"""


def upper_lower_count():
    sentence = input("Enter the sentence string \n ")
    upper_counter = 0
    lower_counter = 0
    for item in sentence:
        if item.isupper():
            upper_counter += 1
        elif item.islower():
            lower_counter += 1
    print(f"No of upper case letters is {upper_counter}")
    print(f"No of lower case letters is {lower_counter}")


"""
Write a Python function that checks whether a word or phrase is palindrome or not.
"""


def word_pallindrome():
    word = input("Enter the word  \n ")
    if word == word[::-1]:
        print(f"The word {word} is a pallindrome")
    else:
        print(f"The word {word} is not a pallindrome")


"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
"""


def ispangram(alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    sentence = input("Enter the sentence \n ")
    myset = set(sentence.replace(" ", "").lower())
    if len(myset) != 26:
        print(
            f"This sentence is not a pangram, the unique letter count is {len(myset)}"
        )
    elif len(myset) == 26:
        if myset == alphaset:
            print("Hurray, this is pangram")
        else:
            print(
                "This is not a pangram, one or more characters might not be alphabets"
            )


"""Longest substring without repeating characters"""


def longestSubString():
    giveninput = input(
        "Enter the string to find longest substring in it without repeated characters: "
    )
    subStringsArray=[]
    mydict={}
    subString = ''
    for mychar in giveninput:
        for item in giveninput:
            if item not in mydict:
                subString = subString + item
                mydict[item] = 1
            else:
                subStringsArray.append(subString)
                subString = ''
                mydict={}
                giveninput=giveninput[1:]
                break;
    longest_SubString=max(subStringsArray,key=len)
    print(" \nThe substrings with out repeated chars are : ")
    print(subStringsArray)
    print('And the longest substring among them is : '+ longest_SubString)

def validParenthesis():
    def isValid():
        s = input("Enter the string which contains only parenthesis: ")
        mydict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for char in s:
            if char in mydict.values():
                stack.append(char)
            elif char in mydict.keys():
                if not stack or stack.pop() != mydict[char]:
                    return False

        return not stack
    if isValid():
        print("Yay ! Input string contains balanced parenthesis")
    else :
        print("Nope ! Input string doesn't contains balanced parenthesis")