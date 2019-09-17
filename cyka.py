# Human Simultor 2000x

# Importera modulerna som behövs
import random, time

# Sätt variablerna
sleeping = True
smell = 1
smellText = "bad"
shower = 1
showerLoop = True
# 
if random.randint(1, 2) == 1:
    smell = 1
    smellText = "bad"
else:
    smell = 2
    smellText = "good"

while sleeping == True:
    wakeup = random.randint(1, 10)
    if wakeup == 4:
        sleeping = False
    else:
        print("zzz")
        time.sleep(1)

print("Good Morning Vietnamn")

if input("You smell " + smellText + ". Wanna shower? y/N") == "y":
    print("You enter the shower. Good!")
    while showerLoop == True:
        if random.randint(1, 10) == 1:
            print("GG You've successfully showered, I bet your mommy would be pround of you.")
            showerLoop = False
            shower = 1
        else:
            if input("Damn you still not done.. Wanna continue? y/N") == "y":
                print("You contine, you obviously don't want to ruin your reputation.")
            else:
                print("Well you tried atleast ._.")
                showerLoop = False
else:
    shower = 2
    print("Oof, well you save time atleast.")

print(sleeping, smell, smellText, shower, showerLoop)