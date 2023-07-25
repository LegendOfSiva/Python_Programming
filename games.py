from random import shuffle


def heads_or_tails():
    list = ["heads", "tails"]
    option = input("What's the call ? \n ")
    shuffle(list)
    if option.lower() == list[0]:
        print(f"That's a {option} indeed , the coin falls as {list}")
    else:
        print(f"oops you lost the toss , the coin falls as {list}")


def guess_the_cup():
    newlist = ["Ball", "", ""]

    def shuffledlist(list):
        shuffle(list)
        return list

    def userguess():
        guess = input("Guess any option from 1 to 3 \n")
        return int(guess)

    def guesscorrect(mylist, guess):
        if mylist[guess - 1] == "Ball":
            print(f"THAT's correct correct answer {mylist}")
        else:
            print(f"That's a wrong guess . the ball is in this cup {mylist}")

    scrambledList = shuffledlist(newlist)
    option = userguess()
    guesscorrect(scrambledList, option)
