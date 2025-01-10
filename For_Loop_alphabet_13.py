# *       *
# * *   * *
# *   *   *
# *       *
# *       *

for row in range(5):
    for col in range(5):
        if col==0 or row==5 or col==4 or row==5 or col==2 and row==2 or row==1 and col==3 or row==1 and col==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()