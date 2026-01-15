#MDunn Lab 9

#GitHub Test Comment

#Define Functions

def convertFarenheit_Celcius(f):
    c = (f - 32) * (5/9)
    return c

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
    elif x==5:
       print("Insert the current temperature in Farenheit. ")
       f = float(input())
       c = convertFarenheit_Celcius(f)
       print (c)

    elif x==4:
        y=101
        while (y>=0) and (y>=100):
            y = float(input("Enter a number between 0 and 100 "))
if (x<67):
    y = float(input("Your guess is too low. Try again."))
if (x>67):
    y = float(input("Your guess is too high. Try again."))
if (y == 67):
    print("Winner, winner, chicken dinner")
if (y<0) or (y>100):
    print("Your guess is not within the requested range.")  

