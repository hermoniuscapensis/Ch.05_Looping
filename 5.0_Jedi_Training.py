  #Sign your name:Julie

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x
print("The total is:", total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

for i in range(2,101,2):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
x = 11
while x>0:
    x-=1
    print(x)
print("Blast off!")


'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
print(random.randrange(1,11))





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
pos = 0
neg = 0
zer = 0
for i in range(7):
    num = int(input("Put in a number!"))
    total+=num
    if num > 0  == 0:
        pos+=1
    elif num == 0:
        zer+=1
    else:
        neg+=1
print("Your total is",total)
print("The number of positive entries is", pos)
print("The number of negative entries is", neg)
print("The number of entries equal to zero is", zer)
