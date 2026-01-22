#MDunn Lab 10

#GitHub test comment


#Randomizer

import random


#Define Functions

def convertFarenheit_Celcius(f):
    c = (f - 32) * (5/9)
    return c

def ro_sham_bo():
    options = ["ro", "sham", "bo"]
    computer_choice = random.choice(options)
    return computer_choice

#Main Program

name=input("What is your name? ")

print("Hello",name)

print("Choose Your Own Adventure")

print("___________________________")

print("Adventure 1: I'll make you laugh.")

print("Adventure 2: I'll tell you the sweetest sound.")

print("Adventure 3: I'll make you smarter.")

print("Adventure 4: Find out if you're lucky!")

print("Adventure 5: Enter the black box ^^")

print("Adventure 6: Let's play Ro-Sham-Bo")

print("___________________________")

x=3
print("Hello",name)

while (x>0) and (x<4):
    x=float(input("Select a number to start your adventure "))

    if x==1:
        print("Six-Seven? That's not what your mom said!")
    elif x==2:
        print(name)
        for i in range(15):
            print(name)
    elif x==3:
        IQ=int(input("Enter your IQ "))
        for i in range(IQ):
            print("It always seems impossible until it is done. – Nelson Mandela")
    elif x==4:
        print("Let's find out if you're lucky :D")
        y=101
        while (y != 67):
            y = int(input("Enter a number between 0 and 100 "))
            if (y<67):
                print("Your guess is too low. Try again.")
            if (y>67):
                print("Your guess is too high. Try again.")
            if (y ==67):
                print("Winner, winner, chicken dinner")
            if (y<0) or (y>100):
                print("Your guess is not within the requested range.")  
    elif x==5:
        print("Insert the current temperature in Farenheit. ")
        f = float(input())
        c = convertFarenheit_Celcius(f)
        print (c)
    elif x == 6:
        print("Let's play Ro-Sham-Bo!")
        print("Type 'end' to quit.")
        options = ["ro", "sham", "bo"]
        y = ""
    while y != "end":
        y = input("Choose ro, sham, or bo: ")
        computer_choice = ro_sham_bo()
        print("Computer chose:", computer_choice)
        if y == computer_choice:
            print("You tied. Try again.")
        elif y == "ro" and computer_choice == "sham":
            print("Sorry, you lost. Sham beats ro.")
        elif y == "ro" and computer_choice == "bo":
            print("You're a winner. Ro beats bo.")
        elif y == "sham" and computer_choice == "bo":
            print("Sorry, you lost. Bo beats sham.")
        elif y == "sham" and computer_choice == "ro":
            print("You're a winner. Sham beats ro.")
        elif y == "bo" and computer_choice == "ro":
            print("Sorry, you lost. Ro beats bo.")
        elif y == "bo" and computer_choice == "sham":
            print("You're a winner. Bo beats sham.")

