#MDunn Final #1


print("Choose Your Own Adventure")

print("___________________________")

print("Adventure 1: I'll make you laugh.")

print("Adventure 2: How hungry are you?.")

print("Adventure 3: Find the loneliest number.")

print("___________________________")

x=3

while (x>0) and (x<4):
    x=float(input("Select a number to start your adventure "))
    if x==1:
        name = input("What is your name? ")
        print("Why did ",name, "bring a ladder to school? Because", name,"wanted to go to high school.")

    elif x==2:
        food = input("What is your favorite food?")
        
        for i in range(20):
            print(food)

    elif x==3:
        print("There is one number that is different from all other numbers.")
        y=101
        while (y != 0):
            y = int(input("What is a number that isn't negative or positive?")) 
            if (y ==0):
                print("You are correct!")
            if (y<0) or (y>0):
                print("Your answer is incorrect. Try again!")  
       
