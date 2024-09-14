import random 
number=random.randint (1,10)
print("WeLcOmE to the gussing game")
print ("enter a ramdome number between 1 and 10,")
print("IF YOU DARE")
while True:
    guess=int(input("GIVE ME A NUMBER BTWEEN 1 AND 10, GOOD LUCK   "))
    if number==guess:
        print("GOOD JOB, HERE IS 100,000,000,0000 DOLLORS")
        print("the number that you gusees is right",guess)
        break
    else:
        print("YOU LOSE, YOU ARE VERY POOR NOW, WHOMP WHOMP")