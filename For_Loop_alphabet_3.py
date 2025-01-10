# *  *  *   
# *
# *
# *
# *  *  *          

for row in range(5):
    for col in range(3):
        if row==0 or col==5 or col==0 or col==5 or col==4 or row==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
