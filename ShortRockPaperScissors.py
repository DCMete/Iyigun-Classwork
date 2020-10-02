import random
rock, paper, scissors, p2 = 1, 2, 3, random.randint(1,3)
p1 = input("p1: ")
if p1 == p2:
    print ("tie")
else:
    print ("p%d won" % ((p1-p2)%3))
