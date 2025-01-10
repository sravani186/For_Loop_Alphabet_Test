# *  *  *
# *
# *  *  *
# * 
# *  *  *

for row in range(5):
    for col in range(3):
        if row==0 or col==3 or col==4 or row==4 or col==0 or row==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()