# * * * *
# *     *
# *   *
# * * 
# *   * 
# *     *
# * * * *    

for row in range(7):
    for col in range(4):
        if row==0 or row==6 or col==0 or row==7 or col+row==4 or col-row==-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()