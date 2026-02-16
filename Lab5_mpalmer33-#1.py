'''
Dice Rolling Terms,
Melissa Palmer,
rolls two dice, prints the outcome, and then uses conditional statements 
to print the appropriate term for that roll based on the table below.,
2/15/2026.

'''

import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2

print("Die 1:", die1)
print("Die 2:", die2)
print("Total:",total)

if die1 == 1 and die2 ==1 :
    print("Snake Eyes")
elif(die1 == 1 and die2 == 2) or (die1 == 2 and die2 == 1 ):
    print("Ace Caught a Deuce")
elif die1 == 2 and die2 == 2:
    print("Little Joe from Kokomo")

