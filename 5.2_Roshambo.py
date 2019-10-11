'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
done = False
win = 0
loss = 0
tie = 0
def winfunction(w):
    print("you won")
    w += 1
    return w
def lossfunction(l):
    print("you lost")
    l += 1
    return l
while not done:
    # user
    Q = int(input("What is your choice? \n 1. rock \n 2. paper \n 3. scissors \n 4. quit \n "))
    if Q == 1:
        print("you chose rock")
    elif Q == 2:
        print("you chose paper")
    elif Q == 3:
        print("you chose scissors")
    elif Q == 4:
        done = True
        print("# of wins:", win)
        print("# of losses:", loss)
        print("# of ties:", tie)
        break
    else:
        print("not an option")
    # computer
    thing2 = random.randrange(1, 4)
    if thing2 == 1:
        print("comp chose rock")
    elif thing2 == 2:
        print("comp chose paper")
    elif thing2 == 3:
        print("comp chose scissors")
    #wins
    if Q == thing2:
        print("tie")
        tie+=1
    elif Q == 2 and thing2 == 1:
        win = winfunction(win)
    elif Q == 1 and thing2 == 3:
        win = winfunction(win)
    else:
        win = winfunction(win)
    #losses
    if Q == 2 and thing2 == 1:
        loss = lossfunction(loss)
    elif Q == 1 and thing2 == 3:
        loss = lossfunction(loss)
    else:
        loss = lossfunction(loss)