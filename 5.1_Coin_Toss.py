'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
HEADS = 0
TAILS = 0
# print(thing)
for i in range(50):
    thing = random.randrange(0, 2)
    if thing == 1:
        HEADS+=1
        print("you got haeds")
    else:
        TAILS+=1
        print("you got tials")
print("# of heads is",HEADS)
print("# of tails is",TAILS)